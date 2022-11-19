#!C:\Users\Pranav\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb,numpy as np,pandas as pd,pickle,mysql.connector,math
cgitb.enable()

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="laptop_data"
)

pipe = pickle.load(open('pipe.pkl','rb'))

print("Context-Type:Text/html\n")

form_inputs=cgi.FieldStorage()
brand=form_inputs.getvalue('brand')
type1=form_inputs.getvalue('type')
ram=form_inputs.getvalue('ram')
wght=form_inputs.getvalue('wght')
touch_screen=form_inputs.getvalue('touch_screen')
ips=form_inputs.getvalue('ips')
screen_size=form_inputs.getvalue('screen_size')
screen_resolution=form_inputs.getvalue('screen_resolution')
cpu=form_inputs.getvalue('cpu')
hdd=form_inputs.getvalue('hdd')
ssd=form_inputs.getvalue('ssd')
gpu=form_inputs.getvalue('gpu')
os=form_inputs.getvalue('os')

ppi="None"
X_res = int((screen_resolution).split('x')[0])
Y_res = int((screen_resolution).split('x')[1])
ppi = str(((X_res**2) + (Y_res**2))**0.5/float(screen_size))

query = np.array([[brand,type1,ram,wght,touch_screen,ips,ppi,cpu,hdd,ssd,gpu,os]])
pred=str(int(np.exp(pipe.predict(query)[0])))


df = pd.read_csv("laptop_data.csv")
prices = df["Price"]
m=0
my_list = [pred]

nearby = list()
for i in prices:
     if i >= int(pred)-1000 and i <= int(pred)+1000:
          my_list.append(i)
#print(my_list)
dbcursor=conn.cursor(buffered=True)

def trunc(number, ndigits=2):
    parts = str(number).split('.')
    truncated_number = '.'.join([parts[0], parts[1][:ndigits]]) 
    return round(float(truncated_number), 2)

print("""
     <!DOCTYPE html>
     <html lang="en">
     <head>
          <title>Laptop Recommendation System</title>
          
          <!-- Google Font: Source Sans Pro -->
          <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">
          <!-- Font Awesome -->
          <link rel="stylesheet" href="plugins/fontawesome-free/css/all.min.css">
          <!-- daterange picker -->
          <link rel="stylesheet" href="plugins/daterangepicker/daterangepicker.css">
          <!-- iCheck for checkboxes and radio inputs -->
          <link rel="stylesheet" href="plugins/icheck-bootstrap/icheck-bootstrap.min.css">
          <!-- Bootstrap Color Picker -->
          <link rel="stylesheet" href="plugins/bootstrap-colorpicker/css/bootstrap-colorpicker.min.css">
          <!-- Tempusdominus Bootstrap 4 -->
          <link rel="stylesheet" href="plugins/tempusdominus-bootstrap-4/css/tempusdominus-bootstrap-4.min.css">
          <!-- Select2 -->
          <link rel="stylesheet" href="plugins/select2/css/select2.min.css">
          <link rel="stylesheet" href="plugins/select2-bootstrap4-theme/select2-bootstrap4.min.css">
          <!-- Bootstrap4 Duallistbox -->
          <link rel="stylesheet" href="plugins/bootstrap4-duallistbox/bootstrap-duallistbox.min.css">
          <!-- BS Stepper -->
          <link rel="stylesheet" href="plugins/bs-stepper/css/bs-stepper.min.css">
          <!-- dropzonejs -->
          <link rel="stylesheet" href="plugins/dropzone/min/dropzone.min.css">
          <!-- Theme style -->
          <link rel="stylesheet" href="dist/css/adminlte.min.css">          
     </head>
     <body style="background-image: url('bg_img.jpg'); position: relative; background-repeat:no-repeat;  background-size:100% 100vh;">          
          <div class="row" style="margin-top: 55px;">
               <div class="col-1"></div>
               <div class="col-10" style="background-color:rgb(255,255,255,0.6); border-radius:15px;">
                    <div class="row">                              
                         <div class="col-12 d-flex justify-content-center">                        
                              <h1>The predicted price for given specifications is <span id="result1"></span></h1>
                         </div>
                    </div>  
                    <hr>
                    <div class="row">
                         <div class="col-12 d-flex justify-content-center">
                              <h3>Some Recommendations in similar price range</h3>
                         </div>
                    </div>
                    <div class="row">""")    
for i in range(1,7):              
     dbcursor.execute("select * from data where Price like '"+str(trunc(my_list[i], 2))+"%'")       
     result = dbcursor.fetchone()
     print("""<div class="col-12 col-sm-6 col-md-4 d-flex align-items-stretch flex-column">
              <div class="card bg-light d-flex flex-fill">
                <div class="card-header text-muted border-bottom-0">                  
                </div>
                <div class="card-body pt-0">
                  <div class="row">
                    <div class="col-12">
                      <h2 class="lead"><b>"""+result[0]+" "+result[1]+" "+str(result[2])+"""</b></h2>
                      <p class="text-muted text-sm"><b>About: </b> """+result[3]+" / "+result[4]+" / "+result[5]+" / "+result[6]+" / "+result[7]+" / "+result[8]+" / "+result[9]+""" </p>                      
                    </div>                    
                  </div>
                </div>
                <div class="card-footer">
                  <div class="text-right">
                    <b class="lead">Price:</b>                    
                    <b class="lead"> &#8377;"""+str(round(result[10]))+"""</b>
                  </div>
                </div>
              </div>
            </div>""")  

print(""" </div>
          <div class="row" style="padding-bottom: 15px;">
               <div class="col-2"></div>
               <div class="col-8">
                    <a href="specifications.py">
                         <button type="button" class="btn btn-block btn-outline-info btn-sm">Try Different Specifications</button>
                    </a>
               </div>
               <div class="col-2"></div>
          </div>
          </div>                 
          <div class="col-1"></div>                                           
          </div>      
          <!-- jQuery -->
          <script src="plugins/jquery/jquery.min.js"></script>
          <!-- Bootstrap 4 -->
          <script src="plugins/bootstrap/js/bootstrap.bundle.min.js"></script>
          <!-- Select2 -->
          <script src="plugins/select2/js/select2.full.min.js"></script>
          <!-- Bootstrap4 Duallistbox -->
          <script src="plugins/bootstrap4-duallistbox/jquery.bootstrap-duallistbox.min.js"></script>
          <!-- InputMask -->
          <script src="plugins/moment/moment.min.js"></script>
          <script src="plugins/inputmask/jquery.inputmask.min.js"></script>
          <!-- date-range-picker -->
          <script src="plugins/daterangepicker/daterangepicker.js"></script>
          <!-- bootstrap color picker -->
          <script src="plugins/bootstrap-colorpicker/js/bootstrap-colorpicker.min.js"></script>
          <!-- Tempusdominus Bootstrap 4 -->
          <script src="plugins/tempusdominus-bootstrap-4/js/tempusdominus-bootstrap-4.min.js"></script>
          <!-- Bootstrap Switch -->
          <script src="plugins/bootstrap-switch/js/bootstrap-switch.min.js"></script>
          <!-- BS-Stepper -->
          <script src="plugins/bs-stepper/js/bs-stepper.min.js"></script>
          <!-- dropzonejs -->
          <script src="plugins/dropzone/min/dropzone.min.js"></script>
          <!-- AdminLTE App -->
          <script src="dist/js/adminlte.min.js"></script>
          <!-- AdminLTE for demo purposes -->
          <script src="dist/js/demo.js"></script>
          <!-- Page specific script -->
          <script>

          var number = """+pred+""";
          document.getElementById('result1').innerHTML = number.toLocaleString('en-IN', {
          maximumFractionDigits: 2,
          style: 'currency',
          currency: 'INR'
          });

          $(function () {
          //Initialize Select2 Elements
          $('.select2').select2()

          //Initialize Select2 Elements
          $('.select2bs4').select2({
               theme: 'bootstrap4'
          })

          //Datemask dd/mm/yyyy
          $('#datemask').inputmask('dd/mm/yyyy', { 'placeholder': 'dd/mm/yyyy' })
          //Datemask2 mm/dd/yyyy
          $('#datemask2').inputmask('mm/dd/yyyy', { 'placeholder': 'mm/dd/yyyy' })
          //Money Euro
          $('[data-mask]').inputmask()

          //Date picker
          $('#reservationdate').datetimepicker({
               format: 'L'
          });

          //Date and time picker
          $('#reservationdatetime').datetimepicker({ icons: { time: 'far fa-clock' } });

          //Date range picker
          $('#reservation').daterangepicker()
          //Date range picker with time picker
          $('#reservationtime').daterangepicker({
               timePicker: true,
               timePickerIncrement: 30,
               locale: {
               format: 'MM/DD/YYYY hh:mm A'
               }
          })
          //Date range as a button
          $('#daterange-btn').daterangepicker(
               {
               ranges   : {
                    'Today'       : [moment(), moment()],
                    'Yesterday'   : [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
                    'Last 7 Days' : [moment().subtract(6, 'days'), moment()],
                    'Last 30 Days': [moment().subtract(29, 'days'), moment()],
                    'This Month'  : [moment().startOf('month'), moment().endOf('month')],
                    'Last Month'  : [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
               },
               startDate: moment().subtract(29, 'days'),
               endDate  : moment()
               },
               function (start, end) {
               $('#reportrange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'))
               }
          )

          //Timepicker
          $('#timepicker').datetimepicker({
               format: 'LT'
          })

          //Bootstrap Duallistbox
          $('.duallistbox').bootstrapDualListbox()

          //Colorpicker
          $('.my-colorpicker1').colorpicker()
          //color picker with addon
          $('.my-colorpicker2').colorpicker()

          $('.my-colorpicker2').on('colorpickerChange', function(event) {
               $('.my-colorpicker2 .fa-square').css('color', event.color.toString());
          })

          $("input[data-bootstrap-switch]").each(function(){
               $(this).bootstrapSwitch('state', $(this).prop('checked'));
          })

          })
          // BS-Stepper Init
          document.addEventListener('DOMContentLoaded', function () {
          window.stepper = new Stepper(document.querySelector('.bs-stepper'))
          })

          // DropzoneJS Demo Code Start
          Dropzone.autoDiscover = false

          // Get the template HTML and remove it from the doumenthe template HTML and remove it from the doument
          var previewNode = document.querySelector("#template")
          previewNode.id = ""
          var previewTemplate = previewNode.parentNode.innerHTML
          previewNode.parentNode.removeChild(previewNode)

          var myDropzone = new Dropzone(document.body, { // Make the whole body a dropzone
          url: "/target-url", // Set the url
          thumbnailWidth: 80,
          thumbnailHeight: 80,
          parallelUploads: 20,
          previewTemplate: previewTemplate,
          autoQueue: false, // Make sure the files aren't queued until manually added
          previewsContainer: "#previews", // Define the container to display the previews
          clickable: ".fileinput-button" // Define the element that should be used as click trigger to select files.
          })

          myDropzone.on("addedfile", function(file) {
          // Hookup the start button
          file.previewElement.querySelector(".start").onclick = function() { myDropzone.enqueueFile(file) }
          })

          // Update the total progress bar
          myDropzone.on("totaluploadprogress", function(progress) {
          document.querySelector("#total-progress .progress-bar").style.width = progress + "%"
          })

          myDropzone.on("sending", function(file) {
          // Show the total progress bar when upload starts
          document.querySelector("#total-progress").style.opacity = "1"
          // And disable the start button
          file.previewElement.querySelector(".start").setAttribute("disabled", "disabled")
          })

          // Hide the total progress bar when nothing's uploading anymore
          myDropzone.on("queuecomplete", function(progress) {
          document.querySelector("#total-progress").style.opacity = "0"
          })

          // Setup the buttons for all transfers
          // The "add files" button doesn't need to be setup because the config
          // `clickable` has already been specified.
          document.querySelector("#actions .start").onclick = function() {
          myDropzone.enqueueFiles(myDropzone.getFilesWithStatus(Dropzone.ADDED))
          }
          document.querySelector("#actions .cancel").onclick = function() {
          myDropzone.removeAllFiles(true)
          }
          // DropzoneJS Demo Code End
          </script>
     </body>
     </html>""")
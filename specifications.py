#!C:\Users\Pranav\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb,model
cgitb.enable()
model.createModule()

print("Context-Type:Text/html\n")

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
          <form name="form" action="price_prediction.py" method="post">
               <div class="row" style="margin-top: 15px; color:white;">
                    <div class="col-12">
                         <h1 class="text-center">Laptop Specifications</h1>
                    </div>
               </div>
               <div class="row">
                    <div class="col-1"></div>
                    <div class="col-10" style="background-color:rgb(255,255,255,0.7); border-radius:15px; background-size: cover;">
                         <div class="row" style="margin-top: 15px; margin-bottom: 15px;">
                              <div class="col-4" >
                                   <div class="form-group">
                                        <label>Brand</label>
                                        <select class="form-control select2 select2-success" data-dropdown-css-class="select2-success" name="brand">
                                             <option selected="selected" value="Apple">Apple</option>
                                             <option value="HP">HP</option>
                                             <option value="Acer">Acer</option>
                                             <option value="Asus">Asus</option>
                                             <option value="Dell">Dell</option>
                                             <option value="Lenovo">Lenovo</option>
                                             <option value="Chuwi">Chuwi</option>
                                             <option value="MSI">MSI</option>
                                             <option value="Microsoft">Microsoft</option>
                                             <option value="Toshiba">Toshiba</option>
                                             <option value="Huawei">Huawei</option>
                                             <option value="Xiaomi">Xiaomi</option>
                                             <option value="Vero">Vero</option>
                                             <option value="Razer">Razer</option>
                                             <option value="Mediacom">Mediacom</option>
                                             <option value="Samsung">Samsung</option>
                                             <option value="Google">Google</option>
                                             <option value="Fujitsu">Fujitsu</option>
                                             <option value="LG">LG</option>
                                        </select>
                                   </div>
                              <!-- /.form-group -->
                              </div>
                              <div class="col-4" >
                                   <div class="form-group">
                                        <label>Type</label>
                                        <select class="form-control select2 select2-success" data-dropdown-css-class="select2-success" name="type">
                                             <option selected="selected" value="Notebook">Notebook</option>
                                             <option value="Ultrabook">Ultrabook</option>
                                             <option value="Netbook">Netbook</option>
                                             <option value="Gaming">Gaming</option>
                                             <option value="2 in 1 convertable">2 in 1 convertable</option>
                                             <option value="Workstation">Workstation</option>
                                        </select>
                                   </div>
                              <!-- /.form-group -->
                              </div>
                              <div class="col-4" >
                                   <div class="form-group">
                                        <label>RAM (in GB)</label>
                                        <select class="form-control select2 select2-success" data-dropdown-css-class="select2-success" name="ram">
                                             <option selected="selected" value="2">2</option>
                                             <option value="4">4</option>
                                             <option value="8">8</option>
                                             <option value="12">12</option>
                                             <option value="16">16</option>
                                             <option value="24">24</option>
                                             <option value="32">32</option>
                                             <option value="64">64</option>
                                        </select>
                                   </div>
                              <!-- /.form-group -->
                              </div>    
                         </div>
                         <div class="row" style="margin-top: 15px; margin-bottom: 15px;">
                              <div class="col-4" >
                                   <div class="form-group">
                                        <label>Weight of the laptop</label>
                                        <input type="number" class="form-control" id="exampleInputEmail1" placeholder="in kg" step="0.01" name="wght" required>
                                   </div>
                              <!-- /.form-group -->
                              </div>
                              <div class="col-4" >
                                   <div class="form-group">
                                        <label>Touch Screen</label>
                                        <select class="form-control select2 select2-success" data-dropdown-css-class="select2-success" name="touch_screen">
                                             <option selected="selected" value="0">No</option>
                                             <option value="1">Yes</option>                                        
                                        </select>
                                   </div>
                              <!-- /.form-group -->
                              </div>
                              <div class="col-4" >
                                   <div class="form-group">
                                        <label>IPS</label>
                                        <select class="form-control select2 select2-success" data-dropdown-css-class="select2-success" name="ips">
                                             <option selected="selected" value="0">No</option>
                                             <option value="1">Yes</option>
                                        </select>
                                   </div>
                              <!-- /.form-group -->
                              </div>                                             
                         </div>
                         <div class="row" style="margin-top: 15px; margin-bottom: 15px;">
                              <div class="col-4" >
                                   <div class="form-group">
                                        <label>Screen size</label>
                                        <input type="number" class="form-control" id="exampleInputEmail1" placeholder="in inch" step="0.01" name="screen_size" required>
                                   </div>
                              <!-- /.form-group -->
                              </div>
                              <div class="col-4" >
                                   <div class="form-group">
                                        <label>Screen resolution</label>
                                        <select class="form-control select2 select2-success" data-dropdown-css-class="select2-success" name="screen_resolution">
                                             <option selected="selected" value="1920x1080">1920x1080</option>
                                             <option value="1366x768">1366x768</option>
                                             <option value="1600x900">1600x900</option>
                                             <option value="3840x2160">3840x2160</option>
                                             <option value="3200x1800">3200x1800</option>
                                             <option value="2880x1800">2880x1800</option>
                                             <option value="2560x1600">2560x1600</option>                      
                                             <option value="2560x1440">2560x1440</option>                
                                             <option value="3200x1800">3200x1800</option>
                                        </select>
                                   </div>
                              <!-- /.form-group -->
                              </div>
                              <div class="col-4" >
                                   <div class="form-group">
                                        <label>CPU</label>
                                        <select class="form-control select2 select2-success" data-dropdown-css-class="select2-success" name="cpu">
                                             <option selected="selected" value="Intel Core i3">Intel Core i3</option>
                                             <option value="Intel Core i5">Intel Core i5</option>
                                             <option value="Intel Core i7">Intel Core i7</option>
                                             <option value="AMD Processor">AMD Processor</option>
                                             <option value="Other Intel Processor">Other Intel Processor</option>                                       
                                        </select>
                                   </div>
                              <!-- /.form-group -->
                              </div>                                             
                         </div>
                         <div class="row" style="margin-top: 15px; margin-bottom: 15px;">
                              <div class="col-4" >
                                   <div class="form-group">
                                        <label>HDD (in GB)</label>                                   
                                        <select class="form-control select2 select2-success" data-dropdown-css-class="select2-success" name="hdd">
                                             <option selected="selected" value="0">0</option>
                                             <option value="128">128</option>
                                             <option value="256">256</option>
                                             <option value="512">512</option>
                                             <option value="1024">1024</option>
                                             <option value="2048">2048</option>
                                        </select>
                                   </div>
                              <!-- /.form-group -->
                              </div>
                              <div class="col-4" >
                                   <div class="form-group">
                                        <label>SSD (in GB)</label>
                                        <select class="form-control select2 select2-success" data-dropdown-css-class="select2-success" name="ssd">
                                             <option selected="selected" value="0">0</option>
                                             <option value="8">8</option>
                                             <option value="128">128</option>
                                             <option value="256">256</option>
                                             <option value="512">512</option>
                                             <option value="1024">1024</option>
                                        </select>
                                   </div>
                              <!-- /.form-group -->
                              </div>
                              <div class="col-4" >
                                   <div class="form-group">
                                        <label>GPU</label>
                                        <select class="form-control select2 select2-success" data-dropdown-css-class="select2-success" name="gpu">
                                             <option selected="selected" value="Nvidia">Nvidia</option>
                                             <option value="Intel">Intel</option>
                                             <option value="AMD">AMD</option>                                        
                                        </select>
                                   </div>
                              <!-- /.form-group -->
                              </div>                                             
                         </div>
                         <div class="row" style="margin-top: 15px; margin-bottom: 15px;">
                              <div class="col-4" ></div>
                              <div class="col-4" >
                                   <div class="form-group">
                                        <label>OS</label>
                                        <select class="form-control select2 select2-success" data-dropdown-css-class="select2-success" name="os">
                                             <option selected="selected" value="Windows">Windows</option>
                                             <option value="Mac">Mac</option>
                                             <option value="Other">Other</option>                                        
                                        </select>
                                   </div>
                              <!-- /.form-group -->
                              </div>
                              <div class="col-4" ></div>                                             
                         </div>                                                                            
                         <div class="row" style="margin-top: 15px; margin-bottom: 15px;">
                              <div class="col-4"></div>
                              <div class="col-4">
                                   <button type="submit" style="width:100%" class="btn btn-outline-primary">Submit</button>
                              </div>
                              <div class="col-4"></div>
                         </div>
                    </div>
                    <div class="col-1"></div>
               </div> 
          </form>    
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

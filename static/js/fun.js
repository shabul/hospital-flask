function login()
    {
       $("#warning-invalid-in").hide()
        $("#warning-expired").hide()
       var username = $('#lusername').val();
       var password = $('#lpassword').val();
       var project=$('#project_name').val();
       localStorage.setItem("x", project);
       localStorage.setItem("username",username);
       console.log(username,password,project); 

       $.ajax({
             type: "POST",
             crossDomain: true,	
             url: "/get_creds",
             data: JSON.stringify({'username':username, 'password':password, 'project':project}),
             processData: false,
             contentType: false,
             success: function(response)
             {
    
                 console.log(response);
                 if(response == "allow"){
                     console.log("Auth verfied");
                 window.location.href  = '/index';
                
    
                 }
                 else if(response=="dont_allow"){
                        
                     // alert("Invalid User Name or Password");
                     $("#warning-invalid-in").show();
    
                 }
                 else{
                 //     alert("Project Expired");
                     $("#warning-expired").show();
                 }
            },
            error: function() 
            {
                console.log('error');
            }
            
        });
    }
        
        
        function signup()
        {
            $('#warning-invalid-up').hide()
            $('#warning-exist').hide()
            
           var username = $('#susername').val();
           var password = $('#spassword').val();
            
           // localStorage.setItem("x", username);
           console.log(username, password);
           $.ajax({
                 type: "POST",
                 crossDomain: true,	
                 url: "/signup_creds",
                 data: JSON.stringify({'username':username, 'password':password}),
                 processData: false,
                 contentType: false,
                 success: function(response)
                 {
        
                    // $('#warning-login').hide()
                     console.log(response);
                     if(response == "allow"){
                         console.log("Auth verfied");
                        container.classList.add("pass-page");
                     }
                     else if(response=="invalid"){
                            // window.location.href  = '/',
                            // $('#warning-login-load').hide()
                            
                         $('#warning-exist').show()
                         // alert("User Name already exist");
                            // console.log("error");
                     }
                     else{
                         $('#warning-invalid-up').show()
                         // alert("Invalid User Name or Password");
                     }
                },
                error: function() 
                {
                    console.log('error');
                }
                
            });
            
            // var user1=localStorage.getItem("x");
            var user1=document.getElementById("susername").value;
            document.getElementById("username1").value=user1;
        }
        
        function pass()
        {
            $('#warning-pass').hide()
            $('#warning-pass-long').hide()
            var user=document.getElementById("susername").value;
            // var user=localStorage.getItem("x");
            var old_password=$('#Opassword').val();
            var new_password=$('#Npassword').val();
            var confirm_password=$('#Cpassword').val();
            console.log(user,old_password,new_password,confirm_password);
            
            if(new_password.length<8)
            {  
            $('#warning-pass-long').show()
            // alert("Password must be at least 8 characters long.");
            return false;  
            }
            else if(confirm_password!=new_password){
            $('#warning-pass').show()
            // alert("Password doesn't match")
            return false;
            }
            
            $.ajax({
                 type: "POST",
                 crossDomain: true,	
                 url: "/chgpass_creds",
                 data:JSON.stringify({'username':user,'Oopassword':old_password,'Nnpassword':new_password,'Ccpassword':confirm_password}),
                 processData: false,
                 contentType: false,
                 success: function(response)
                 {
                    // $('#warning-login').hide()
                     console.log(response);
                     if(response == "allow"){
                         console.log("Auth verfied");
                         container.classList.remove("pass-page");
                         container.classList.remove("right-panel-active");
                         
                     }
                     else{
                            $('#warning-pass').show()
                            // alert("Invalid Password");
                            // $('#warning-login').show()
                            
                     }
                },
                error: function() 
                {
                    console.log('error');
                }
                
            });
        }

       
    $(document).ready(function() {
    $('#lusername').change(function() {
        var ccusername = $('#lusername').val();
        
        $("#project_name").empty();
        $("#project_name").append($(document.createElement('option')).prop({
                         value:"",
                         text:"Project Name",
                         selected:true,
                         disabled:true,
                         hidden:true
                  }))
        
        $.ajax({
                 type: "POST",
                 crossDomain: true,
                 url: "/get_proj_name",
                 data: JSON.stringify({'username':ccusername}),
                 processData: false,
                 contentType: false,
                 success:function(response)
                {
                    console.log(response);
                    var values=response;
                    var c=1;
                 
        for (const val of values) {
            if(c==1){
            $('#project_name').append($(document.createElement('option')).prop({
                value: val,
                text: val.charAt(0).toUpperCase() + val.slice(1),
                selected:true
            }))
            }
            else{
            $('#project_name').append($(document.createElement('option')).prop({
                value: val,
                text: val.charAt(0).toUpperCase() + val.slice(1)
                }))
            }
            c=c+1
        }
        
                },
            error: function() 
                {
                    console.log('error');
                }
        
        
        
        
        });
           })
});



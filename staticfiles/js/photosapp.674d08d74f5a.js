function copyFunction() {
    /* Get the text field */
    var copyLink = document.getElementById("photoLink");
  
    /* Select the text field */
    copyLink.select();
    copyLink.setSelectionRange(0, 99999); /*For mobile devices*/
  
    /* Copy the text inside the text field */
    document.execCommand("copy"); 
    
  }
  

  $(document).ready(function(){
      $("#shareButton").click(function(){
          $(".copy-alert").empty();
          $(".copy-alert").append(`<div class="alert alert-dismissible" role="alert">
                                    <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                                    <p>Image link copied to clipboard!</p>
                                </div>`);
      });     
      
  });
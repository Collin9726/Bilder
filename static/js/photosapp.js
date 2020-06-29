function copyFunction(id_value) {
    /* Get the text field */
    var copyLink = document.getElementById(id_value);
  
    /* Select the text field */
    copyLink.select();
    copyLink.setSelectionRange(0, 99999); /*For mobile devices*/
  
    /* Copy the text inside the text field */
    document.execCommand("copy"); 
    
  }
  

  $(document).ready(function(){
      $("button.shareButton").click(function(){
          alert("Image link has been copied to clipboard!")          
      });     
      
  });
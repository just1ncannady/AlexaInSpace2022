// For new popups, change title and html below and change noshow number in code below twice by incrementing it by 1. It might be better to delete this file and upload a new one, because editing here doesn't seem to always take.
$( function() {
    $('<div/>', {
    'id':'dialog',
    'title': 'Mobile CSP Curriculum Updates & PDs',
    'html':'Register for  Mobile CSP Professional Development    <p><a style="text-decoration:none;text-align:center;background-color:#597db1;color:white;padding:5px;border-radius:5px;" href="https://mobile-csp.org/participate" target="_blank">Mobile CSP PDs</a><p>See the <a href="https://docs.google.com/document/d/1kpKG7KMA2p118vrba9MT7F_pYGqoEJjpYagCMzn9qTY/edit?usp=sharing" target="_blank"><u>Change Log</u></a> for a list of curriculum updates! <p><input type=checkbox id=disable>Don\'t show again</p>',
    
}).appendTo('body');  
      
  
      
    $.ui.dialog.prototype._focusTabbable = $.noop; // gets rid of 1st link focused default
      
   // For NEW popups, change the noshow number below
    if (localStorage.noshow5)
      $( "#dialog" ).hide();
    else 
        $( "#dialog" ).dialog();
    
    
    $("#disable").change( function() {   // checkbox checked
        // For NEW popups, change the noshow number below
        localStorage.noshow5 = true;
    });
    
  } );

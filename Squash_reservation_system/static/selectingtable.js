$(".column100").click( function(event) {
           if(confirm("Are you sure you want to reserve this hour?")){
               $(this).attr("class", "gray");
           }
           else{
               return false;
           }
});

$("td.column2,td.column3,td.column4,td.column5,td.column6,td.column7,td.column8").click( function(event) {
           if(confirm("Are you sure you want to reserve this hour?")){
               $(this).attr("class", "gray");
           }
           else{
               return false;
           }
});

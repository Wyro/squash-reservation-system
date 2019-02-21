$("td.column2,td.column3,td.column4,td.column5,td.column6,td.column7,td.column8").click( function(event) {
           //if(confirm("Are you sure you want to reserve this hour?")){
               //$(this).attr("class", "gray");
          if($('input[name=selected_time]').attr("value",$(this).siblings().eq(0).html().split(' ')[0])){
            //console.log($(this).index())
            //console.log($('th').eq($(this).index()).html());
            $('input[name=selected_day]').attr("value",$('th').eq($(this).index()).html())
          }
          else{
               return false;
          }
});

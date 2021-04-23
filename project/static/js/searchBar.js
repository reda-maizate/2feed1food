let button = $("#searchBar");

button.on('click',function (){
   $.ajax({
       method:"POST",
       url: "/index/post",
       data:{
           'query' : $("#searchQuery").val(),
       },
       success: function (response){
            $("#context").html(response);
       }
   })
});
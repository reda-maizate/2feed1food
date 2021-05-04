const nextButtons = $("[id^='next']");
const prevButtons = $("[id^='previous']");

for (const prevButton of prevButtons) {
    makeItListen($(prevButton), -1);
}

for (const nextButton of nextButtons) {
    makeItListen($(nextButton), 1);
}



function makeItListen($button, addOrReduce){

    const category = $button.data("category");
    const origin = $($button).data("origin");

    const id = $button.attr('id');
    let tableau = $("#collapseN" + category);

    $button.on('click',  function () {
        $.ajax({
            url : '/score/ajax',
            method : 'POST',
            data : {
                grade : category,
                origin : Math.max(0,origin + (10 * addOrReduce)),
            },
            success: function (html){
                $(tableau).replaceWith(html);


                makeItListen($("#next"+ category) , 1 );
                makeItListen($("#previous"+ category) , -1 );
                $("#collapseN" + category).addClass('show');
            }
        });
    });


}
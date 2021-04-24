let button = $("#searchBar");

button.on('click', function () {

    let form = $("#esForm");
    let switchesState = {
        'query': $("#searchQuery").val(),
    }

    switchesState = manageOrderInput(form, switchesState);
    switchesState = manageAllergenInput(form, switchesState);

    $.ajax({
        method: "POST",
        url: "/index/post",
        data: switchesState,
        success: function (response) {
            $("#context").html(response);
        }
    })
});

function manageOrderInput(form, switchesState){
    form.find("input[name]").each(function () {
        if ($(this).is(':checked')) {
            switchesState[this.name] = $(this).attr("asc_or_desc");
        }
    });

    return switchesState
}

function manageAllergenInput(form, switchesState){
    form.find("input[with]").each(function () {
        if ($(this).is(':checked')) {
            switchesState[$(this).attr("word")] = $(this).attr("with");
        }
    });

    return switchesState
}
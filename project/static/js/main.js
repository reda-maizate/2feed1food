
let ajaxChart = new Chart($("#myChart3"),
{ 
    data: {
        labels: [],
        datasets: [],
    },
    type: 'bar',
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
    
});

$('#ajaxSubmit').on('click', function(){
    ajaxChart.labels = [];
    ajaxChart.data.datasets = [];
    
    $(".searchBlock").addClass('foundBlock').removeClass('d-none searchBlock');

    $.ajax({
        type: 'POST',
        url: 'get',
        data: {
            param : $("#ajaxSearch").val(),
        },
        
        success: function(response){
            ajaxChart.data.labels = response.labels;
            ajaxChart.data.datasets.push(response.data);

            ajaxChart.update();
        }
    })
});

$("#ajaxErase").on('click' , function(){
    console.log("yep");
    $(".foundBlock").addClass('d-none searchBlock').removeClass('foundBlock');

    ajaxChart.data.labels = [];
    ajaxChart.data.datasets = [];

    ajaxChart.update();
});
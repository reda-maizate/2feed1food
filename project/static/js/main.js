
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
    removeData(ajaxChart);
    
    $(".searchBlock").addClass('foundBlock').removeClass('d-none searchBlock');

    $.ajax({
        type: 'POST',
        url: 'get',
        data: {
            param : $("#ajaxSearch").val(),
        },
        
        success: function(response){
            // ajaxChart.data.labels = response.labels;
            // ajaxChart.data.datasets.push(response.data[0]);

            addData(ajaxChart , response.labels , response.data)
            ajaxChart.update();
        }
    })
});

$("#ajaxErase").on('click' , function(){
    console.log("yep");
    $(".foundBlock").addClass('d-none searchBlock').removeClass('foundBlock');

    removeData(ajaxChart);
});


function addData(chart, labels, data) {
    chart.data.labels = labels;

    for (let i = 0 ; i < data.length ; i++) {
        console.log(data[i]);
        chart.data.datasets.push(data[i]);
    }

    chart.update();
}

function removeData(chart) {
    chart.data.labels = [];
    chart.data.datasets = [];

    chart.update();
}
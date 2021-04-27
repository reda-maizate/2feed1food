let canva = $("#myChart3");
let ajaxChart = new Chart(canva,
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

$('#ajaxSubmit').on('click', function (button) {
    removeData(ajaxChart);

    $(".searchBlock").addClass('foundBlock').removeClass('d-none searchBlock');

    $.ajax({
        type: 'POST',
        url: 'get',
        data: {
            param: $("#ajaxSearch").val(),
        },

        success: function (response) {
            if (response.hasOwnProperty('error') && response.error === true) {
                $("#errorPlace").html(response.message);
                hideCanva()
            } else {
                $("#errorPlace").html("");

                addData(ajaxChart, response.labels, response.data)
                ajaxChart.update();
            }
        }
    })
});

$("#ajaxErase").on('click', hideCanva);


function hideCanva() {
    $(".foundBlock").addClass('d-none searchBlock').removeClass('foundBlock');

    removeData(ajaxChart);
}

function addData(chart, labels, data) {
    chart.data.labels = labels;

    for (let i = 0; i < data.length; i++) {
        chart.data.datasets.push(data[i]);
    }

    chart.update();
}

function removeData(chart) {
    chart.data.labels = [];
    chart.data.datasets = [];

    chart.update();
}
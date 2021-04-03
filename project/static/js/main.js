let ctx = $('#myChart1');
let ctx2 = $('#myChart2');

let ctx3 = $('#myChart3');

const values = [1,2,3,2,3,4,2];

let myLineChart = new Chart(ctx, {
    type: 'line',
    data: values,
    options: {},
});


const values2 = [3,4,1,2,3,2,2];

let myChart = new Chart(ctx2, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
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
    $.ajax({
        type: 'POST',
        url: 'test4',
        data: {
            param : $("#ajaxSearch").val(),
        },
        
        success: function(response){
            new Chart($("#myChart3"),
            { 
                type: 'bar',
                data: {
                    labels:  response.cols,
                    datasets: [{
                        label: 'prices',
                        data: response.data,
                    }],
                },
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
        }
    })
});
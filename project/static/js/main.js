let ctx = $('#myChart1');
let ctx2 = $('#myChart2');

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
        url: 'test4',
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

const labels = ['lun', 'mar' , 'mer' , 'jeu' , 'ven' , 'sam' , 'dim'];
const data = {
    labels: labels,
    datasets: [{
      label: 'My First Dataset',
      data: [65, 59, 80, 81, 56, 55, 40],
      fill: false,
      borderColor: 'rgb(75, 192, 192)',
      tension: 0.1
    }]
}
const config = {
    type: 'line',
    data: data,
};

var myLineChart = new Chart(ctx, {
    type: 'line',
    data: data,
    options: {}
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
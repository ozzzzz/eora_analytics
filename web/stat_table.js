window.onload = function () {

var dpoints = [];

var chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	theme: "light2",

	title:{
		text:"Fortune 500 Companies by Country"
	},
	axisX:{
		interval: 1
	},

	data: [{
		type: "bar",
		name: "companies",
		axisYType: "secondary",
		// color: "#014D65",
		dataPoints: dpoints
	}]
});



function updateChart(){
	function addData(data) {
		chart.options.data[0].dataPoints = data;
		chart.render();
	}

	$.getJSON("http://127.0.0.1:5000/stats", addData);
}

updateChart()

setInterval(function() {updateChart()}, 150000);


$("#mkChinaGreatAgain").click(function () {
	console.log("!")
	var objIndex = chart.options.data[0].dataPoints.findIndex((obj => obj.label == 'China'));
	var objValue = chart.options.data[0].dataPoints[objIndex].y
	chart.options.data[0].dataPoints[objIndex].y = objValue + 1

	chart.options.data[0].dataPoints
	  .sort(
    	function(a, b){
    		return a.y - b.y;
    	})
	  .map(function(p) {
	  delete p.x;
	  return p
	});

	chart.render();
})

}
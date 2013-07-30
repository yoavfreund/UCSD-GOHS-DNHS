/*
Created by: Ajay Nathan
Created on: July 29, 2013
Last modified: 7/2013
*/

var dataset = [];	//defines an empty dataset
for(var i = 0; i < (Math.round(Math.random() * 15) + 10); i++) {
	var newNumber = (Math.round(Math.random() * 30));
	dataset.push(newNumber);	//fills dataset with up to 25 random integers less than 30
}

var h = 230;	//sets height of visual (in px)
var w = 1400;	//sets width of visual (in px)
var barPadding = 5;	//sets spacing between bars (in px)

var scaleHeight = d3.scale.linear()
				.domain([0, 30])
				.rangeRound([21, h]);	//sets scale based on height

var svg = d3.select("body")
          	.append("svg")
		.attr("xmlns", "http://www.w3.org/2000/svg")
		.attr("version", "1.2")
		.attr("width", w)
		.attr("height", h);	//creates svg

var rectangles = svg.selectAll("rect")
		 	.data(dataset)
			.enter()
			.append("rect")
			.attr("height", 
				function(d) {
					return scaleHeight(d) + "px";
				})
			.attr("width", ((w / dataset.length) - barPadding))
			.attr("x",
				function(d,i) {
					return (i * (w / dataset.length)) + "px";
				})
			.attr("y",
				function(d) {
					height = scaleHeight(d);
					return (h - height) + "px";
				})
			.attr("fill",
				function(d) {
					return "rgb(0, " + (d * 5) + ", " + (d * 8) + ")";
				});	//creates a bar graph based on data (up to 25 rectangles with height proportional to data point)

var text = svg.selectAll("text")
		.data(dataset)
		.enter()
		.append("text")
		.text(
			function(d) {
				return d;
			})
		.attr("x",
			function(d,i) {
				return ((i * w / dataset.length) + (w / dataset.length - barPadding) / 2);
			})
		.attr("y",
			function(d) {
				return ((h - scaleHeight(d)) + 17);
			})
		.attr("text-anchor", "middle")
		.attr("font-size", "16px")
		.attr("fill", "white");

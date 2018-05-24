var svgWidth1 = 960/3;
var svgHeight1 = 500/2;


var svgWidth2 = 960/3;
var svgHeight2 = 500/2;

var svgWidth3 = 960;
var svgHeight3 = 650;

var margin3 = {
  top: 20/2,
  right: 40/2,
  bottom: 80/2,
  left: 100/2
};

var margin2 = {
  top: 20/2,
  right: 40/2,
  bottom: 80/2,
  left: 100/2
};

var margin1 = {
  top: 20/2,
  right: 40/2,
  bottom: 80/2,
  left: 100/2
};

var width1 = svgWidth1 - margin1.left - margin1.right;
var height1 = svgHeight1 - margin1.top - margin1.bottom;


var width2 = svgWidth2 - margin2.left - margin2.right;
var height2 = svgHeight2 - margin2.top - margin2.bottom;

var width3 = svgWidth3 - margin3.left - margin3.right;
var height3 = svgHeight3 - margin3.top - margin3.bottom;


// Create an SVG wrapper, append an SVG group that will hold our chart,
//and shift the latter by left and top margins.
var svg1 = d3
  .select(".chart1")
  .append("svg")
  .attr("width", svgWidth1)
  .attr("height", svgHeight1)

  var svg2 = d3
  .select(".chart2")
  .append("svg")
  .attr("width", svgWidth2)
  .attr("height", svgHeight2)

  var svg3 = d3
  .select(".chart3")
  .append("svg")
  .attr("width", svgWidth3)
  .attr("height", svgHeight3)
  
// Append an SVG group
var chartGroup1 = svg1.append("g")
  .attr("transform", `translate(${margin1.left}, ${margin1.top})`);

var chartGroup2 = svg2.append("g")
  .attr("transform", `translate(${margin2.left}, ${margin2.top})`);

var chartGroup3 = svg3.append("g")
  .attr("transform", `translate(${margin3.left}, ${margin3.top})`);

// Initial Params
var chosenXAxis = "poverty"

// function used for updating x-scale var upon click on axis label
function xScale(healthData, chosenXAxis) {
  // create scales
  var xLinearScale = d3.scaleLinear()
    .domain([d3.min(healthData, d => d[chosenXAxis]) * 0.8,
      d3.max(healthData, d => d[chosenXAxis]) * 1.2
    ])
    .range([0, width1])

  return xLinearScale

};
function xScale1(healthData, chosenXAxis) {
  // create scales
  var xLinearScale = d3.scaleLinear()
    .domain([d3.min(healthData, d => d[chosenXAxis]) * 0.8,
      d3.max(healthData, d => d[chosenXAxis]) * 1.2
    ])
    .range([0, width3])

  return xLinearScale

};

// function used for updating xAxis var upon click on axis label
function renderAxes(newXScale, xAxis) {
  var bottomAxis = d3.axisBottom(newXScale)

  xAxis.transition()
    .duration(1000)
    .call(bottomAxis)

  return xAxis
}

// function used for updating circles group with a transition to
// new circles
function renderCircles(circlesGroup, newXScale, chosenXaxis) {

  circlesGroup.transition()
    .duration(1000)
    .attr("cx", d => newXScale(d[chosenXAxis]))

  return circlesGroup
};

// function used for updating circles group with new tooltip
function updateToolTip(chosenXAxis, circlesGroup) {

   if (chosenXAxis == "poverty") {
     var label = "Health: "
   } else {
     var label = "% below Poverty line: "
   }

  var toolTip = d3.tip()
    .attr("class", "tooltip")
    .offset([80, -60])
    .html(function (d) {
      return (`${d.state}<br>${label} ${d.health}`);
    });

  circlesGroup.call(toolTip);

  circlesGroup.on("mouseover", function (data) {
      toolTip.show(data);
    })
    // onmouseout event
    .on("mouseout", function (data, index) {
      toolTip.hide(data);
    });

  return circlesGroup
}

// Retrieve data from the CSV file and execute everything below
d3.csv("healthData.csv", function (err, healthData) {
  if (err) throw err;
//console.log (healthData)
  // parse data
  healthData.forEach(function (data) {
    data.poverty = +data.poverty;
    data.health = +data.health;
    // data.population = +data.population;
  });

  // xLinearScale function above csv import
  var xLinearScale = xScale(healthData, chosenXAxis)

  var xLinearScale1 = xScale1(healthData, chosenXAxis)

  // Create y scale function
  var yLinearScale = d3.scaleLinear()
    .domain([d3.min(healthData, d => d.health), d3.max(healthData, d => d.health)])
    .range([height1, 0]);
    
    var yLinearScale1 = d3.scaleLinear()
    .domain([d3.min(healthData, d => d.health), d3.max(healthData, d => d.health)])
    .range([height3, 0]);

  // Create initial axis functions
  var bottomAxis = d3.axisBottom(xLinearScale);
  var bottomAxis1 = d3.axisBottom(xLinearScale1);
  var leftAxis = d3.axisLeft(yLinearScale);
var leftAxis1 = d3.axisLeft(yLinearScale1);

  // append x axis
  var xAxis1 = chartGroup1.append("g")
    .classed("x-axis", true)
    .attr("transform", `translate(0, ${height1})`)
    .call(bottomAxis)



 var xAxis2 = chartGroup2.append("g")
    .classed("x-axis", true)
    .attr("transform", `translate(0, ${height2})`)
    .call(bottomAxis)
 
 var xAxis3 = chartGroup3.append("g")
    .classed("x-axis", true)
    .attr("transform", `translate(0, ${height3})`)
    .call(bottomAxis1)

  // append y axis
  chartGroup1.append("g")
    .call(leftAxis)

 // append y axis
  chartGroup2.append("g")
    .call(leftAxis)

  chartGroup3.append("g")
    .call(leftAxis1)
    
  // append initial circles
  var circlesGroup = chartGroup1.selectAll("circle")
    .data(healthData)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d[chosenXAxis]))
    .attr("cy", d => yLinearScale(d.health))
    .attr("r", 5)
    .attr("fill", "red")
    .attr("opacity", 0.5)

    var circlesGroup2 = chartGroup2.selectAll("circle")
    .data(healthData)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d[chosenXAxis]))
    .attr("cy", d => yLinearScale(d.health))
    .attr("r", 5)
    .attr("fill", "red")
    .attr("opacity", 0.5)
    
    var circlesGroup3 = chartGroup3.selectAll("circle")
    .data(healthData)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale1(d[chosenXAxis]))
    .attr("cy", d => yLinearScale1(d.health))
    .attr("r", 5)
    .attr("fill", "red")
    .attr("opacity", 0.5)

  // Create group for  2 x- axis labels
  var labelsGroup1 = chartGroup1.append("g")
    .attr("transform", `translate(${width1/2}, ${height1 + 20})`)

   var labelsGroup2 = chartGroup2.append("g")
    .attr("transform", `translate(${width1/2}, ${height1 + 20})`)
   
   var labelsGroup3 = chartGroup3.append("g")
    .attr("transform", `translate(${width3/2}, ${height3 + 20})`)

  var povertyLabel1 = labelsGroup1.append("text")
    .attr("x", 0)
    .attr("y", 20)
    .attr("value", "poverty") //value to grab for event listener
    .classed("active", true)
    .text("Below Poverty line (in %)");


  var povertyLabel2 = labelsGroup2.append("text")
    .attr("x", 0)
    .attr("y", 20)
    .attr("value", "poverty") //value to grab for event listener
    .classed("active", true)
    .text("Below Poverty line (in %)");
    
  var povertyLabel3 = labelsGroup3.append("text")
    .attr("x", 0)
    .attr("y", 20)
    .attr("value", "poverty") //value to grab for event listener
    .classed("active", true)
    .text("Below Poverty line (in %)");

//  var albumsLabel = labelsGroup.append("text")
//    .attr("x", 0)
//    .attr("y", 40)
//    .attr("value", "health") //value to grab for event listener
////    .classed("inactive", true)
//    .text("Total Health");

  // append y axis
  chartGroup1.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin1.left)
    .attr("x", 0 - (height1 / 2))
    .attr("dy", "1em")
    .classed("axis-text", true)
    .text("Health Score");
  chartGroup2.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin1.left)
    .attr("x", 0 - (height1 / 2))
    .attr("dy", "1em")
    .classed("axis-text", true)
    .text("Health Score");
    
    chartGroup3.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin1.left)
    .attr("x", 0 - (height1 / 2))
    .attr("dy", "1em")
    .classed("axis-text", true)
    .text("Health Score");

  // updateToolTip function above csv import
  var circlesGroup = updateToolTip(chosenXAxis, circlesGroup)

  // x axis labels event listener
//  labelsGroup.selectAll("text")
//    .on("click", function () {
//      // get value of selection
//      var value = d3.select(this).attr("value")
//      if (value != chosenXAxis) {
//
//        // replaces chosenXAxis with value
//        chosenXAxis = value;
//
//        // console.log(chosenXAxis)

        // functions here found above csv import
        // updates x scale for new data
        xLinearScale = xScale(healthData, chosenXAxis);

        // updates x axis with transition
        xAxis = renderAxes(xLinearScale, xAxis);

        // updates circles with new x values
        circlesGroup = renderCircles(circlesGroup, xLinearScale, chosenXAxis);

        // updates tooltips with new info
        circlesGroup = updateToolTip(chosenXAxis, circlesGroup);

        

    });
//};


import React, { Component } from 'react';
import '../../node_modules/react-vis/dist/style.css';
//import data for wordcloud
import {globalArray} from './data.js';
//import data for scatterplot
import {linedata1} from './linegraphdata1.js';
import {linedata2} from './linegraphdata2.js';
import {linedata4} from './linegraphdata4.js';
import WordCloud from "react-d3-cloud";
import {XYPlot, XAxis, YAxis, HorizontalGridLines, MarkSeries,VerticalBarSeries} from 'react-vis';

const fontSizeMapper = word => Math.log2(word.value) * 5;
const rotate = word => word.value % 360;

//data for bar graph
const barGraphData =[
  {x: 'Length', y: 142},
  {x: 'Most', y: 15},
  {x: 'Average', y: 9},
  {x: 'Unique', y: 68},
  {x: 'WeightLength', y: 43},
	{x: 'WeightUnique', y: 68}	
];

//integrate visualization
class Dashboard extends Component {

    render() {
        return (
            <div >
                <div style={{'text-align': 'center'}}>
                    <div style={{display: 'inline-block'}}>
			<h2>Wordcloud of popular words in songs</h2>
			<WordCloud data={globalArray} fontSizeMapper={fontSizeMapper} width="500" height="500"/>,
			<br/>
			<br/>

	  	  	<h2>Length of song vs popularity</h2>
	  	   <XYPlot
	        width={500}
	        height={500}>
			<XAxis>Length of Song</XAxis>
			<YAxis>Score</YAxis>
	        <MarkSeries
	          className="mark-series-example"
	          sizeRange={[.5, .5]}
			  color="maroon"
	          data={linedata1}/>
	      	</XYPlot>		
				 <br/>
			  <br/>



          <h2>Most repeated words vs popularity</h2>
         <XYPlot
          width={500}
          height={500}>
      <XAxis>Length of Song</XAxis>
      <YAxis>Score</YAxis>
          <MarkSeries
            className="mark-series-example"
            sizeRange={[.5, .5]}
        color="red"
            data={linedata2}/>
          </XYPlot>   
         <br/>
        <br/>



          <h2>Unique words vs popularity</h2>
         <XYPlot
          width={500}
          height={500}>
      <XAxis>Length of Song</XAxis>
      <YAxis>Score</YAxis>
          <MarkSeries
            className="mark-series-example"
            sizeRange={[.5, .5]}
        color="orange"
            data={linedata4}/>
          </XYPlot>   
         <br/>
        <br/>
			  	  	  	<h2>Features in dataset</h2>
		  
  	  	   <XYPlot xType="ordinal"
			  width={500} 
  	        height={500}>
  			<XAxis>Features in Dataset</XAxis>
  			<YAxis>Average</YAxis>
  	        <VerticalBarSeries
  	          className="bar-series-example"
  	          data={barGraphData}/>
  	      	</XYPlot>
                    </div>
                </div>
            </div>
        )
    }
}

export default Dashboard;

.. raw:: html 

   <div class="logo-header"  id="student-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

Visualizing Data
================

.. raw:: html

    <!-- Custom Scripts -->
    <script src="../_static/assets/lib/lessons/tipped.js" type="text/javascript"></script>
    <script src="../_static/assets/lib/lessons/Framework2020.js" type="text/javascript"></script>
    <link href="../_static/assets/lib/lessons/tipped.css" rel="stylesheet" type="text/css"></link>
    <link href="../_static/assets/lib/lessons/lessons.css" rel="stylesheet" type="text/css"></link>
    <link href="../_static/assets/css/custom.css" rel="stylesheet" type="test/css"></link>
    <script src="../_static/assets/lib/lessons/vocabulary.js" type="text/javascript"></script>
    <style>    td { text-align: left; padding: 5px;}</style>


.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
        $(document).ready(function() {
            generateSummary(EKmapping['7.03']);
        generateHovers();
    
    
        });
    </script>
    <h3 id="est-length">Time Estimate: 45 minutes</h3>
    

Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <p>In lesson <a href="../unit?unit=26&amp;lesson=87" target="_blank">7.2 Big Data</a>, we investigated large data sets and how to process them. In this lesson, we will create our own data visualizations using charts in Google Sheets and maps using Google My Maps.
    </p>
	<div><b>Learning Objectives:</b>&nbspI will learn to</div>
	<ul>
	<li>describe what information can be extracted from data and metadata</li>
	<li>identify how a visualization can be used to mislead the audience about its underlying data</li>
	<li>use software to create visualizations</li>
	</ul>
	<div><b>Language Objectives:</b>&nbspI will be able to</div>
	<ul>
	<li>explain insights and knowledge gained from programs and visualizations that process data</li>
	<li>use target vocabulary, such as data, metadata, and correlation while interpreting and creating visualizations, with the support of concept definitions from this lesson</li>
	</ul>

    

Learning Activities
--------------------

.. raw:: html

    <p><h3>Activity 1: Interpret Data Visualizations</h3>
    
    Working with a partner,  explore the following visualization(or another visualization that your teacher suggests) and answer the following questions. <br/>
    <img class="yui-img" height="400px" src="../_static/assets/img/infographic.gif"/> <br/>
    <ol>
    <li style="margin-bottom: 5px;">What is the data shown in this visualization?</li>
    <li style="margin-bottom: 5px;">What type of data is used — text, numbers, geocodes, date and time, etc.?</li>
    <li style="margin-bottom: 5px;">What conclusions can you draw from the data?</li>
    <li style="margin-bottom: 5px;">How is the data presented in the visualization that makes it easy to understand and use?
      </li>
    <li>What are the drawbacks of this visualization?</li></ol>
    <br/><br/>
	<p>Watch and discuss the TED-Ed video below on how data can also be manipulated in data visualizations.
    
    
.. youtube:: E91bGT9BjYk
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    Sometimes we see a <b>correlation</b> between two variables, where they rise and fall in values in parallel ways, for example ice cream sales and shark attacks in the graph below. A <b>correlation</b> is a statistical measure that indicates that two or more variables fluctuate together. However, a correlation found in data does not necessarily indicate that a causal relationship exists. Correlation does not equal <b>causation</b>. Additional research is needed to see whether and how the two variables are related.<br/>
    <img class="yui-img" src="../_static/assets/img/correlation.png" width="50%"></img>
	</p>
	
	<h3>Activity 2: Google Sheets</h3>
    <p>Programs such as spreadsheets can be used in an iterative and interactive way to gain insight and knowledge from data.
    A <b>spreadsheet</b> is a document where the data is arranged in rows and columns. Spreadsheets allow formulas to be used to make calculations from the data and charting capabilities. Spreadsheet programs can also be used to filter and clean digital data. We will be using Google Sheets in Google Drive as our spreadsheet software in the following project.
    </p>
    <ol>
    <li style="margin-bottom: 5px;">
        Open and copy the <a href="https://docs.google.com/spreadsheets/d/12fRy-mhBAhj-6GlHi9y-5tKlkBo7OeSgcWzAKgIXQ30/copy" target="_blank">Astraptes Butterflies data set</a> into your Google Drive. Your instructor may ask you to do File/Move to move the file to a certain folder on your drive or to Share it.  </li>
    <li style="margin-bottom: 5px;">
    This data set shows butterfly specimens captured and tagged in the Guanacaste National Park in Costa Rica.  Look through the data and notice that the first column (herbivore species) is the species of each butterfly that was tagged. The last columns show the latitude and longitude  where each butterfly was tagged. The first row is metadata that describes the data in each column. <b>Metadata</b> is data about data. It can be associated with the primary data, and changes and deletions made to metadata do not change the primary data. Metadata allows data to be structured and organized and is used for finding, organizing and managing information. Metadata can increase the effective use of data or data sets by providing additional information about various aspects of that data. </li>
    <li style="margin-bottom: 5px;">
    <p>
	<img src="../_static/assets/img/cell.png" width="50%" style="float:right"/>
    <b>Formulas and Functions.</b> Each box in the spreadsheet is called a  <b>cell</b>. Every cell  in the spreadsheet is identifiable by its column letter and row number. For example, cell <b>A2</b> refers to the box at column A and row 2 below and contains the data Astraptes SENNOV which is a butterfly species.  
    </p>
	<p>
      We can manipulate numeric data in a spreadsheet by using <b>formulas</b> and <b>functions</b> built into the spreadsheet software. Typing in a <b>=</b> in a cell signals the start of a formula like <b>=K2 + K3</b> or a function like <b>=SUM(K2,K3)</b>. These functions can take a list of cells or a range of cells such as <b>K2:K4</b> which is equivalent to the list <b>K2, K3, K4</b>. There are many built-in functions in standard spreadsheet software, but the most commonly used ones are SUM, AVERAGE, COUNT, MAX, and MIN. Here is a <a href="https://www.gcflearnfree.org/googlespreadsheets/working-with-functions/1/" target="_blank">tutorial</a> that reviews how to use functions in Google Sheets.</p>
    
    Let’s use a formula to calculate the average wingspan of the butterflies in our spreadsheet. 
       Column <b>K</b> contains the wingspan measurement of each butterfly.
    <ul>
    <li style="padding-bottom:5px">Scroll down to the empty cell K89 (column K, row 89).</li>
    <li>Type in the formula:
      <b>
        =AVERAGE(K2:K88)</b> like below. This will average the data in column K rows 2-88. You could select the data that you want instead of typing in the cell numbers. When you hit enter, it will compute the average 54.63 (you can control the precision with the precision buttons in the toolbar at the top). <br/>
    <img src="../_static/assets/img/formula.png" width="50%" style="display:block; margin-left: auto; margin-right: auto;"/>
    </li>
    <li> (<b>Portfolio)</b> Write another formula that calculates the <b>average elevation</b> for this data. Write your formula and the result found in your portfolio.
         </li>
    </ul>
    </li>
    <li><img src="../_static/assets/img/filterSheets.png" style="float:right; padding-left:5px" width="45%"/>
    <b>Sort and Filter:</b>
        You can sort and filter columns to find information and extract patterns from the data. To sort by species, click on the A at the top of column A to select the column, and then from the Data menu (or the drop down menu on column A), choose Sort. To undo the sort, select Edit/Undo. 
    
    <p>You can also filter data to show only the data you need. Click on column E or any column that you want to filter, and then click on Data/Create a Filter or the filter funnel icon <img src="../_static/assets/img/filterIcon.png" width="20px"/> to turn on filtering. Click on the filter icon created in cell E1 and uncheck Blanks and male, to leave just the female values. Click on OK to see the filtered data. Turn off filtering by clicking on the filter funnel icon or from the Data menu to go back to seeing all the data. 
     
        </p><p>To help, here’s a <a href="https://edu.gcfglobal.org/en/googlespreadsheets/sorting-and-filtering-data/1/" target="_blank">sorting and filtering tutorial</a>.
      </p></li>
    <li style="margin-bottom: 5px;"><b>Charts:</b> Let’s make a chart to visualize some of the data in this spreadsheet. 
    <ul>
    <li style="margin-bottom: 5px;">Click on the A heading in the first column (herbivore species).  </li>
    <li style="margin-bottom: 5px;">From the Insert menu at the top, select Chart.  
    You will see a bar chart of the different species found in column A. </li>
    <li style="margin-bottom: 5px;">Investigate the many chart options available. Try a pie chart like below. Here’s more information about <a href="https://support.google.com/docs/answer/190718" target="_blank">different charts in Google Sheets</a> and a <a href="http://www.mathgoodies.com/lessons/graphs/compare_graphs.html" target="_blank">tutorial on comparing charts</a>.
    <br/><img src="../_static/assets/img/chart.png" width="80%" style="display:block; margin-left: auto; margin-right: auto;"/>
    </li>
    <li style="margin-bottom: 5px;"> The chart can help us answer questions such as which species is the most common? 
    </li><li> Once you are finished designing your chart, you can click on the dots in the top right corner of the chart to copy the image or move it to its own sheet.</li>
    </ul>
    </li><li> Make new charts to answer the following questions:
    <ul>
    <li style="margin-bottom: 5px;">  (<b>Portfolio</b>) Are there more male or female butterflies in this data set? Include a screenshot of your chart in your portfolio to answer this question. What kind of data is in your chart?
      </li>
    <li style="margin-bottom: 5px;">(<b>Portfolio</b>) Which ecological environment (primary eco column) do these butterflies like to live in? There is no clear winner in this question so give the percentages in each ecological environment in a screenshot of your chart and describe the data in your portfolio.
      </li>
    <li>(<b>Portfolio</b>) Come up with a 3rd question and use charting to answer it. Include a screenshot of your chart in your portfolio to answer this question. What kind of data is in your chart?</li>
    </ul>
    </li>
    </ol>
    <h3>Activity 3: Google Maps</h3>
    The last columns in the spreadsheet contain location data, latitudes and longitude in which the butterflies were found.  We can map this data using Google My Maps. For troubleshooting in this activity, refer to the <a href="https://support.google.com/mymaps/#topic=3188329" target="_blank">Google My Maps Help Center</a>
    <ol>
    <li style="margin-bottom: 5px;">
         Go to <a href="http://www.google.com/mymaps" target="_blank">http://www.google.com/mymaps</a> and click on the Create A New Map button. The created map will be saved in your Google Drive.
       </li><li style="margin-bottom: 5px;">Change the <em>Untitled Map</em> heading to a title like <em>Butterflies Map</em> and click on the blue Import button.
    <br/>
    <img src="../_static/assets/img/map1.png" width="50%"style="display:block; margin-left: auto; margin-right: auto;border:1px solid"/>
    </li><li style="margin-bottom: 5px;">Click on Google Drive and find your spreadsheet.
    <br/>
    <img src="../_static/assets/img/map2.png" width="50%" style="display:block; margin-left: auto; margin-right: auto;border:1px solid"/>
    </li><li style="margin-bottom: 5px;">Scroll down to select the Latitude and Longitude columns.
    <br/>
    <img src="../_static/assets/img/map3.png" width="50%" style="display:block; margin-left: auto; margin-right: auto;border:1px solid"/>
    </li><li style="margin-bottom: 5px;">Pick the herbivore species column as the title for the placemarks.
    Google maps will place your data set as markers on the map. Click on some of the markers to see your data. Click on the paint roller icon to group places by herbivore species or by another column like primary eco and add labels from one of the columns, and click on the paintcan to choose different icons.
       <br/>
    <img src="../_static/assets/img/maplabel.png" width="50%" style="display:block; margin-left: auto; margin-right: auto;border:1px solid"/>
    </li><li style="margin-bottom: 5px;">Click on Share to share your map with your teacher or to change the settings to anyone with the link can view. 
       </li><li>(<b>Portfolio</b>) Copy the link to your portfolio. Click on Preview to grab a screenshot of your map to put in your portfolio.
    </li></ol>
    
Summary
--------

.. raw:: html

    <p>
    In this lesson, you learned how to:
      <div id="summarylist">
    </div>
    
Still Curious?
---------------

.. raw:: html

    <p>These <a href="https://think.cs.vt.edu/corgis/visualizer/index.html" target="_blank">Visualizer Data Sets</a> allow you to create visualizations of their data sets with different types of graphs.</p>


Self-Check
-----------

.. raw:: html

    <p>
    <h3>Sample AP CSP Exam Question</h3>
    
.. mchoice:: mcsp-7-3-1
    :random:
    :practice: T
    :answer_a:  Approximately how many miles did the animal travel in one week?
    :feedback_a: 
    :answer_b:  Does the animal travel in groups with other tracked animals?
    :feedback_b: 
    :answer_c:  Do the movement patterns of the animal vary according to the weather?
    :feedback_c: This is correct.
    :answer_d:  In what geographic locations does the animal typically travel?
    :feedback_d: 
    :correct: c

    .. raw:: html
    
    	<p>Biologists often attach tracking collars to wild animals. For each animal, the following geolocation data is collected at frequent intervals.</p>
    	<ul>
    		<li>The time</li>
    		<li>The date</li>
    		<li>The location of the animal</li>
    	</ul>
    	<p>Which of the following questions about a particular animal could <b>NOT</b> be answered using only the data collected from the tracking collars?</p>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <br/>
    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/174UVUg14VsnFE0G1TKXSXDvpZPIVXt1U4T1f97xRfUo/copy" target="_blank" title="">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vQkQFqeoBqH9hsbAq48I8X718yTsTjUkVSsH-_27jMRYlliNMYSBs-kvtUZgkrzOQEYMxUYZVMDPKFD/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!-- Create a  page called &lt;i&gt;Data Visualization&lt;/i&gt; in your portfolio. 
      &lt;ol&gt;
        &lt;li&gt;(&lt;b&gt;Activity 2&lt;/b&gt;) Write a spreadsheet formula that calculates the average &lt;b&gt;elevation&lt;/b&gt; for the data in this spreadsheet. Write your formula and the result found in your portfolio.&lt;/li&gt;
    
        &lt;li&gt;(&lt;b&gt;Activity 2&lt;/b&gt;) Are there more male or female butterflies in this data set? Include a screenshot of your chart to answer this question. What kind of data is in your chart?
        &lt;/li&gt;
    &lt;li&gt;(&lt;b&gt;Activity 2&lt;/b&gt;) Which ecological environment (primary eco column) do these butterflies like to live in? There is no clear winner in this question so give the percentages in each ecological environment in a screenshot of your chart. What kind of data is in your chart?&lt;/li&gt;
    &lt;li&gt;(&lt;b&gt;Activity 2&lt;/b&gt;) Come up with a 3rd question and use charting to answer it. Include the screenshot. What kind of data is in your chart?&lt;/li&gt;
    &lt;li&gt;(&lt;b&gt;Activity 3&lt;/b&gt;) Include a screenshot and link of the map you created for this data.
        &lt;/li&gt;
        &lt;/ol&gt;
     -->
    </div>
    </div>
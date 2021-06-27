MAIN_HTML_MSG = """<!DOCTYPE html>
        <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <title>Coderage</title>
            <link rel="icon" sizes="15x15" href="favicon.png">
            <link rel="stylesheet" href="main_style.css" type="text/css">
            <link rel="stylesheet" href="highchart.css" type="text/css">

        </head>
        <body class="indexfile">
        <div id="header">
            <div class="content">
                <img src="logo.png"></img>
            </div>
        </div>

        <div id="index">
            <table class="index">
                <thead>
                    <tr class="tablehead">
                        <th class="shortkey_s">Run Number</th>
                        <th class="shortkey_s">TestsPath</th>
                        <th class="shortkey_m">Passed</th>
                        <th class="shortkey_x">Failed</th>
                        <th class="right shortkey_c">Errors</th>
                        <th class="right shortkey_c">Skipped</th>
                        <th class="right shortkey_c">Run Time (Sec)</th>
                        <th class="right shortkey_c">Coverage Path</th>
                        <th class="right shortkey_c">Coverage %</th>
                        <th class="right shortkey_c">Statments</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="file">
                        <td class="name left">{main_table[0]}</td>
                        <td>{main_table[1]}</td>
                        <td>{main_table[2]}</td>
                        <td>{main_table[3]}</td>
                        <td>{main_table[4]}</td>
                        <td>{main_table[5]}</td>
                        <td>{main_table[6]}</td>
                        <td>{main_table[7]}</td>
                        <td>{main_table[8]}</td>
                        <td>{main_table[9]}</td>
                    </tr>
                </tbody>
            </table>
            <p id="no_rows">
                No items found using the specified filter.
            </p>
        </div>
        <br></br>
        <br></br>
        
        <table style="width:100%">
              <tr>
                <td> 
                 <div id="footer">
                    <div class="content">
                        <span>
                            <a class="nav" href="detailedLastRun.html">Detailed Last Ran Analysis</a> 
                        </span>
                    </div>
                 </div>
                </td>
                <td> 
                 <div id="footer">
                    <div class="content">
                        <span>
                            <a class="nav" href="pytest_report.html">Detailed Tests Results</a> 
                        </span>
                    </div>
                 </div>
                </td>
                <td> 
                 <div id="footer">
                    <div class="content">
                        <span>
                            <a class="nav" href="index.html">Detailed Coverage</a> 
                        </span>
                    </div>
                 </div>
                </td> 
                <td> 
                 <div id="footer">
                    <div class="content">
                        <span>
                            <a class="nav" href="coverageAnalysis.html">Coverage Analysis By File</a> 
                        </span>
                    </div>
                 </div>
                </td> 
                <td> 
                 <div id="footer">
                    <div class="content">
                        <span>
                            <a class="nav" href="testAnalysis.html">Test Analysis By File</a> 
                        </span>
                    </div>
                 </div>
                </td>                                                
              </tr>
          
          <tr>
            <td style="font-size: 13px;">
                Details about last run - tests & function stats</td>
            <td style="font-size: 13px;">
                HTML test report which python generates</td>
            <td style="font-size: 13px;">
                HTML coverage report which coverage generates</td>
            <td style="font-size: 13px;">
                Coverage percentage by file</td>
            <td style="font-size: 13px;">
                Test statuses and percentage by file</td>
          </tr>
        </table>
        <br></br>

        <script src="https://code.highcharts.com/highcharts.js"></script>
        <script src="https://code.highcharts.com/modules/series-label.js"></script>
        <script src="https://code.highcharts.com/modules/exporting.js"></script>
        <script src="https://code.highcharts.com/modules/export-data.js"></script>
        <script src="https://code.highcharts.com/modules/accessibility.js"></script>
        <script src="https://code.highcharts.com/highcharts-more.js"></script>
        <script src="https://code.highcharts.com/modules/data.js"></script>
        <br></br>
        <br></br>
        <div class="charts">
        <figure class="highcharts-figure">
          <div id="container"></div>
        </figure>
        
        <figure class="highcharts-figure">
          <div id="container3"></div>
        </figure>

        <figure class="highcharts-figure">
          <div id="container2"></div>
        </figure>

        </div>

        <script type="text/javascript" src="highchart.js"></script>
        </body>
        </html>
        """

COVERAGE_HTML_ANALYSIS = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coverage Analysis By File</title>
    <link rel="icon" sizes="15x15" href="favicon.png">
    <style>
    * {{
      box-sizing: border-box;
    }}
    
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu, Cantarell, "Helvetica Neue", sans-serif; font-size: 1em; background: #fff; color: #000; }}

    .parent {{
        display: flex;
        flex-direction: column;
        align-items: center;
        height: 700px;
        max-height: 700px;
    }}

    img {{ width: 20%; height: 20%; margin-left: 40%;}}
    #myInput {{
      background-position: 10px 10px;
      background-repeat: no-repeat;
      width: 50%;
      font-size: 12px;
      padding: 12px 20px 12px 40px;
      border: 1px solid #ddd;
      margin-bottom: 12px;
    }}

    #myTable {{
      border-collapse: collapse;
      width: 50%;
      border: 1px solid #ddd;
      font-size: 12px;
    }}

    #myTable th, #myTable td {{
      text-align: left;
      padding: 12px;
    }}

    #myTable tr {{
      border-bottom: 1px solid #ddd;
    }}

    #myTable tr.header, #myTable tr:hover {{
      background-color: #f1f1f1;
      position: sticky;
    }}
    thead,
    tbody tr {{
        display: table;
        width: 100%;
        }}
    tbody {{
        display: block;
        overflow-y: scroll;
        overflow-x: none;
        max-height: 350px;
    }}
    
    h1{{
        text-align: center;
    }}
    
    </style>
</head>
<body>
<div id="header">
    <div class="content">
        <img src="logo.png"></img>
    </div>
</div>

    <br></br>
    <h1>Coverage Analysis By File</h1>
    <br></br>
    <div class="parent">

    <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for file name.." title="Type in a file name">

    <table id="myTable">
      <tr class="header">
        <th>Run number</th>
        <th>File name</th>
        <th>Coverage Percentages</th>

      </tr>
      <tbody>
          {}
      </tbody>
    </table>

    <script>
    function myFunction() {{
      var input, filter, table, tr, td, i, txtValue;
      input = document.getElementById("myInput");
      filter = input.value.toUpperCase();
      table = document.getElementById("myTable");
      tr = table.getElementsByTagName("tr");
      for (i = 0; i < tr.length; i++) {{
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {{
          txtValue = td.textContent || td.innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {{
            tr[i].style.display = "";
          }} else {{
            tr[i].style.display = "none";
          }}
        }}
      }}
    }}
    </script>
</div>
</body>
</html>"""

DETAILED_LAST_RUN = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
     <link rel="stylesheet" href="detailedLastRun.css" type="text/css">
      <link rel="stylesheet" href="main_style.css" type="text/css">
     <link rel="stylesheet" href="highchart2.css" type="text/css">
     <link rel="icon" sizes="15x15" href="favicon.png">
    <title>Detailed Last Run</title>
    <style>
    h1.detailed{{
        text-align: center;
        display: block;
    }}
    
    #myTable{{
      width: 100%;
      border-collapse:separate; 
      border-spacing:5em;
    }}
        
    #myTable tr{{
      padding-bottom: 1em;
    }}
    
    #myTable #index td{{
       width: 100%;
       text-align:left;
    }}
    
    #index{{
       width: 90%;
    }}
    
    #index th{{
       width: 100%;
       text-align:left;
       background-color:rgb(124, 181, 236);
       color:white;
       font-weight: bold;
    }}
    
    caption {{
    margin-bottom: 5px;
    font-size: 100%;
    padding: 5px;
    font-weight: bold;
    }}
    </style>
    
</head>
<div id="header">
    <div class="content">
        <img src="logo.png"></img>
    </div>
</div>
<body>
    <br></br>
    <h1 class="detailed">Detailed Last Run</h1>
    <br></br>
    <div class="parent">
        <script src="https://code.highcharts.com/highcharts.js"></script>
        <script src="https://code.highcharts.com/modules/exporting.js"></script>
        <script src="https://code.highcharts.com/modules/export-data.js"></script>
        <script src="https://code.highcharts.com/modules/accessibility.js"></script>
        
              
      
       
        <table id="myTable">
        <tr>
        <td colspan="2">
        <figure class="highcharts-figure">
          <div id="container"></div>
        </figure>
        </td>
        </tr>
                
        <tr>
        <td>
        <div class="new">
        <table id="index">
        <caption>Functions not tested:</caption>
                <thead>
                    <tr class="tablehead">
                        <th class="shortkey_s">File name</th>
                        <th class="shortkey_s">Test name</th>
                    </tr>
                </thead>
                <tbody>
                    {}
                </tbody>
            </table>
        </div>
        </td>
        
        <td>
        <div class="test">
                <table id="index">
                <caption>Tests that consistently fail (5 times in a row or More):</caption>
                <thead style="display:table-header-group">
                    <tr class="tablehead">
                        <th class="shortkey_s">Class name</th>
                        <th class="shortkey_s">Test name</th>
                    </tr>
                </thead>
                <tbody>
                    {}
                </tbody>
            </table>
        </div>
        </td>
        </tr>
        
        <tr>
        <td>
        <div class="not">
            <table id="index">
            <caption>Functions that changed status from previous run:</caption>
                <thead style="display:table-header-group">
                    <tr class="tablehead">
                        <th class="shortkey_s">File name</th>
                        <th class="shortkey_s">Function name</th>
                        <th class="shortkey_s">Current run</th>
                        <th class="shortkey_s">Previous run</th>
                    </tr>
                </thead>
                <tbody>
                    {}
                </tbody>
            </table>        
        </div>
        </td>
        
        <td>
        <div class="test">
            <table id="index">
            <caption>Tests that changed status from previous run: </caption>
                <thead style="display:table-header-group">
                    <tr class="tablehead">
                        <th class="shortkey_s">Class name</th>
                        <th class="shortkey_s">Test name</th>
                        <th class="shortkey_s">Current run</th>
                        <th class="shortkey_s">Previous run</th>
                    </tr>
                </thead>
                <tbody>
                    {}
                </tbody>
            </table>
        </div>
        </td>
        </tr>
        
        </table>
    </div>
    <script type="text/javascript" src="highchart2.js"></script>
    <br></br>
</body>
</html>"""

TEST_ANALYSIS =  """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tests Analysis By File</title>
    <link rel="icon" sizes="15x15" href="favicon.png">
    <style>
    * {{
      box-sizing: border-box;
    }}
    
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu, Cantarell, "Helvetica Neue", sans-serif; font-size: 1em; background: #fff; color: #000; }}

    .parent {{
        display: flex;
        flex-direction: column;
        align-items: center;
        height: 300px;
        max-height: 300px;
    }}

    img {{ width: 20%; height: 20%; margin-left: 40%;}}
    #myInput, #myInput2, #myInput3{{
      background-position: 10px 10px;
      background-repeat: no-repeat;
      width: 50%;
      font-size: 12px;
      padding: 12px 20px 12px 40px;
      border: 1px solid #ddd;
      margin-bottom: 12px;
    }}

    #myTable, #myTable2, #myTable3 {{
      border-collapse: collapse;
      width: 90%;
      border: 1px solid #ddd;
      font-size: 12px;
      overflow-y: auto;
    }}

    #myTable th, #myTable2 th, #myTable3 th, #myTable td, #myTable2 td, #myTable3 td {{
      text-align: left;
      padding: 12px;
    }}

    #myTable tr, #myTable2 tr, #myTable3 tr {{
      border-bottom: 1px solid #ddd;
    }}

    #myTable tr.header, #myTable tr:hover, #myTable2 tr.header, #myTable2 tr:hover, #myTable3 tr.header, #myTable3 tr:hover {{
      background-color: #f1f1f1;
      position: sticky;
    }}
    thead,
    tbody tr {{
        display: table;
        width: 100%;
        }}
    tbody {{
        display: block;
        overflow-y: scroll;
        overflow-x: none;
        max-height: 350px;
    }}
    
    h1{{
        text-align: center;
    }}
    
    .row {{
      margin-left:-5px;
      margin-right:-5px;
    }}
      
    .column {{
      float: left;
      width: 33%;
      padding: 5px;
    }}
    
    /* Clearfix (clear floats) */
    .row::after {{
      content: "";
      clear: both;
      display: table;
    }}
    
    </style>
</head>
<body>
<div id="header">
    <div class="content">
        <img src="logo.png"></img>
    </div>
</div>

    <br></br>
    <h1>Tests Analysis By File</h1>
    <br></br>
    
    <div class="parent">
    <div class="row">
    <div class="column">
        <h3>Tested Vs. not Tested</h3>
        <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for file name.." title="Type in a file name">
    
        <table id="myTable">
        <thead>
          <tr class="header">
            <th>Run number</th>
            <th>File name</th>
            <th>Tested Percentages</th>
            <th>Not tested Percentages</th>
          </tr>
        </thead>
        <tbody>
          {}
        </tbody>
        </table>
    
        <script>
        function myFunction() {{
          var input, filter, table, tr, td, i, txtValue;
          input = document.getElementById("myInput");
          filter = input.value.toUpperCase();
          table = document.getElementById("myTable");
          tr = table.getElementsByTagName("tr");
          for (i = 0; i < tr.length; i++) {{
            td = tr[i].getElementsByTagName("td")[1];
            if (td) {{
              txtValue = td.textContent || td.innerText;
              if (txtValue.toUpperCase().indexOf(filter) > -1) {{
                tr[i].style.display = "";
              }} else {{
                tr[i].style.display = "none";
              }}
            }}
          }}
        }}
        </script>
    </div>
      
    <div class="column">
        <h3>Tests status</h3>
        <input type="text" id="myInput2" onkeyup="myFunction2()" placeholder="Search for file name.." title="Type in a file name">
    
        <table id="myTable2">
        <thead>
          <tr class="header">
            <th>Run number</th>
            <th>Class name</th>
            <th>Passed number</th>
            <th>Failed number</th>
          </tr>
        </thead>
        <tbody>
          {}
        </tbody>
        </table>
    
        <script>
        function myFunction2() {{
          var input, filter, table, tr, td, i, txtValue;
          input = document.getElementById("myInput2");
          filter = input.value.toUpperCase();
          table = document.getElementById("myTable2");
          tr = table.getElementsByTagName("tr");
          for (i = 0; i < tr.length; i++) {{
            td = tr[i].getElementsByTagName("td")[1];
            if (td) {{
              txtValue = td.textContent || td.innerText;
              if (txtValue.toUpperCase().indexOf(filter) > -1) {{
                tr[i].style.display = "";
              }} else {{
                tr[i].style.display = "none";
              }}
            }}
          }}
        }}
        </script>
    </div>
    
    <div class="column">
        <h3>Tests That changed status</h3>
        <input type="text" id="myInput3" onkeyup="myFunction3()" placeholder="Search for file name.." title="Type in a file name">
    
        <table id="myTable3">
        <thead>
          <tr class="header">
            <th>Class name</th>
            <th>Test name</th>
            <th>Current run</th>
            <th>Previous run</th>
    
          </tr>
        </thead>
        <tbody>
          {}
        </tbody>
        </table>
    
        <script>
        function myFunction3() {{
          var input, filter, table, tr, td, i, txtValue;
          input = document.getElementById("myInput3");
          filter = input.value.toUpperCase();
          table = document.getElementById("myTable3");
          tr = table.getElementsByTagName("tr");
          for (i = 0; i < tr.length; i++) {{
            td = tr[i].getElementsByTagName("td")[1];
            if (td) {{
              txtValue = td.textContent || td.innerText;
              if (txtValue.toUpperCase().indexOf(filter) > -1) {{
                tr[i].style.display = "";
              }} else {{
                tr[i].style.display = "none";
              }}
            }}
          }}
        }}
        </script>
    </div>
    </div>
    </div>

</body>
</html>"""

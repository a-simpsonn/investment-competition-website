Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investment Club</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 10px 0;
            text-align: center;
        }
        nav {
            display: flex;
            justify-content: center;
            background-color: #333;
        }
        nav a {
            color: white;
            padding: 14px 20px;
            text-decoration: none;
            text-align: center;
        }
        nav a:hover {
            background-color: #ddd;
...             color: black;
...         }
...         main {
...             padding: 20px;
...         }
...         footer {
...             background-color: #333;
...             color: white;
...             text-align: center;
...             padding: 10px 0;
...             position: fixed;
...             width: 100%;
...             bottom: 0;
...         }
...     </style>
... </head>
... <body>
...     <header>
...         <h1>Investment Club</h1>
...     </header>
...     <nav>
...         <a href="#home">Home</a>
...         <a href="#competition">Competition</a>
...         <a href="#apply">Apply</a>
...         <a href="#contact">Contact</a>
...     </nav>
...     <main id="home">
...         <h2>Welcome to the Investment Club</h2>
...         <p>Join us for our exciting investment competition! Learn more below.</p>
...     </main>
...     <main id="competition">
...         <h2>Competition Details</h2>
...         <p>Bauer Capital Group, the University of Houston's undergraduate investment fund, will be hosting the 2nd annual Undergraduate Commodity Competition in October 2024.</p>
...         <p> Competition Overview</p>
...         <p>Each team of four students will select, research and pitch a commodity equity or trade idea to a panel of industry judges. Teams will have fifteen minutes to present their ideas and fifteen minutes for a Q&A. The primary goal of the pitch is to assert a view on a specific commodity market and design a creative way to profit off that view. A critical part of building a thesis in the context is to clearly outline the macroeconomic factors that affect the chosen commodity to explain the speculative view and investment opportunity that exists.</p>
...         <p>Past sponsors have included reputable finacial firms and energy companies including Jefferies, J.P. Morgan, Bank of America, Shell, Mercuria, Evercore, Moelis and more. There will be an energy mixer hosted the evening before the competition to give students the opportunity to interact with industry professionals across finance and energy. </p>
...         <p>All travel and lodging expenses related to the competition will be covered.</p>
...         <p>Applications open on May 31st, 2024. Interviews start on June 10th, 2024. Applications will close on June 17th, 2024.</p>
...     </main>
...     <main id="apply">
...         <h2>Apply to Join</h2>
...         <form action="/submit-application" method="post">
...             <label for="name">Name:</label><br>
...             <input type="text" id="name" name="name"><br>
...             <label for="email">Email:</label><br>
...             <input type="email" id="email" name="email"><br>
...             <label for="phone">Phone Number:</label><br>
...             <input type="tel" id="phone" name="phone"><br>
...             <label for="reason">Why are interested in this investment competition and what do you hope to learn or acheive from this experience?</label><br>
...             <textarea id="reason" name="reason"></textarea><br>
...             <label for="prior experience">Do you have a basic understanding of valuation methodologies (DCF, CCA, PTA, NAV)?</label><br>
...             <textarea id="response" name="response"></textarea><br>
...             <label for="resume">Upload Resume:</label><br>
...             <input type="file" id="resume" name="resume" accept=".pdf,.doc,.docx" required><br>
...             <input type="submit" value="Submit">
...         </form>
...     </main>
...     <main id="contact">
...         <h2>Contact Us</h2>
...         <p>Email: as61967n@pace.edu</p>
...         <p>Phone: 908-357-6208</p>
...     </main>
...     <footer>
...         <p>&copy; 2024 Investment Competition - Finance Club</p>
...     </footer>
... </body>

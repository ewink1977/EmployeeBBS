<h1>Employee BBS & Time Management System</h1>
<p>ewink's Coding Dojo SOLO graduation project!</p>
<h2> It's CRUNCH time!</h2>
<img src="https://www.douglasavenue.com/img/mikucomputer.jpg" alt="Miku at a computer.">
<p> I feel like this is going to be me in a few days, except I won't have anywhere near as much hair, won't be anywhere close to being as adorable as Miku is, and will be a real human male, rather than a fictional girl. So, I guess that's won't be me?</p>
<p>UPDATE: Yeah, it is me, without the kawaii...</p>
<p>Anyway, welcome to the GitRepo for my solo graduation project.</p>
<h2>Concept</h2>
<p>When complete, this project will act as a mini-intranet Twitter style message board for a business' employees. Basically, a digital breakroom corkboard.</p>
<p>Managers at both the department and top tier levels will be able to sticky messages and add events to the system to ensure all users see things that will be affecting them and their departments.</p>
<p>To increase the systems usefulness, there will also be a time management system built into the BBS, allowing employees to clock in and out and track their hours.</p>
<h3>Terminology</h3>
<p>For the purpose of this README, there are three classes of users. <b>Superuser</b> which could be considered top-tier level management (e.g. a store's general manager). <b>Managers</b> which would run departments (e.g. a restaurant's head chef, or a shift supervisor). <b>Employees</b>, which should be considered base-level hourly staff with little or no supervisory role. <i>Admins</i>, for the purpose of this explanation, are both Superusers and Managers. <i>Users</i> are all users of the system, regardless of admin level.</p>
<h2>Functions</h2>
<p>There are three </p>








<h2>Goals</h2>
<p>When complete, the system should:</p>
<ul>
  <li>Allow a user to create an account, and log in with that account. <strong>FEATURE COMPLETE</strong>
    <ul>
      <li>Users will be able to upload a profile picture to use with their account. The will also be able to edit their account information, including changing their username and password.</li>
      <li>Admins will be able to edit user's accounts, including being able to change a user's password (in the case a user forgets it and gets locked out).</li>
    </ul></li>
  <li>Allow a user to post messages that will appear on their and other user's timeline.
   <ul>
     <li>Superusers will be able to sticky messages that will appear to all users, regardless of admin level or department. <strong>FEATURE COMPLETE</strong></li>
     <li>Managers will be able to sticky messages that will appear to only their department. <strong>FEATURE COMPLETE</strong></li>
     <li>Users will be able to like and reply to messages. <strong>FEATURE COMPLETE</strong></li>
     <li>Users will be able to delete their own messages. <strong>FEATURE COMPLETE</strong></li>
     <li>Admins will be able to delete any message. <strong>FEATURE COMPLETE</strong></li>
    </ul></li>
  <li>Admins will be able to post and edit events that will be displayed on the user's homepage. <strong>FEATURE COMPLETE</strong></li>
  <li>Employees and managers will be able to use the system as a basic time management system with a clock-in and clock out option, as well as the ability to edit their timesheets (e.g. in the case they forgot to clock out the night before). Admins will be able to edit any user's timesheet. The timesheet system should add up hours worked.
    <ul>
    <li>It should be noted that TIME MANAGEMENT is a low priority feature which may not be completed on time, in which case it will not be added.</li>
    </ul></li>
  </ul>
<h2>Front-End</h2>
<p>To keep things relatively simple, the front end will be developed using Bootstrap for styling, and will incorporate some jQuery functions, primarily AJAX to basically allow the main page to update without reloading the whole page. Tweaks will appear here and there, which is what this GitHub repo is for - so you can make fun of my tweaks.</p>
<h2>Back-end</h2>
<p>The backend will be built using Django and will utilize multiple python libraries. I will update this more when I have decided how much of the built in Django auth I am going to use and how much I am going to build myself.</p>
<h2>Questions?</h2>
<p>Hit me up at erin@douglasavenue.com</p>
<hr>
<p>Thanks for checking this out!</p>
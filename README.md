<h1>KRK -- The Employee BBS & Time Management System</h1>
<h2>This project is no longer online.</h2>
<hr />
<h2>Introduction</h2>
<p>Welcome to KRK (pronounced 'cork'). </p>
<p>KRK is a virtual corkboard for businesses. I got the idea from back in the pre-Internet era of the early 1990s. I worked at McDonald’s, and in the breakroom, there was a corkboard where people would leave messages for each other, management would post notices, and a calendar was posted that had events and upcoming sales on it.</p>
<h2>Concept</h2>
<p>KRK works to replicate this by creating a Twitter-inspired timeline where employees can post messages, reply to those messages, and favorite them. Supervisors can sticky important department information to the top of the timeline, and store management can post important messages seen by all users.</p>
<p>There is also an event calendar that allows department-level and storewide events to be displayed. Finally, KRK offers a basic Time Management System which allows employees to keep track of their time worked.</p>
<h2>Terminology</h2>
<p>For this README, there are 3 classes of users. To simplify this, we’ll say KRK is being used in a restaurant.</p>
<ul>
  <li><b>Management</b> – This is the top tier management of the facility (e.g., a store’s General Manager).</li>
  <li><b>Supervisors</b> – These are department managers and supervisors (e.g., the head chef, or a front-line shift manager).</li>
  <li><b>Employees</b> – These are the backbone of your staff. Everyone who doesn’t count as Management or Supervisor is an employee. They have the lowest level of access, being restricted to interacting with their own department only.</li>
</ul>
<p>As well, <i>admins</i> cover both Management and Supervisors, as they both have some administrative privileges. <i>Users</i> refers to all users of the system, regardless of class.</p>
<h2>Functions</h2>
<p>Right now, KRK has three main functions – User Management, Posting, and Event Calendar.</p>
<h4>User Management</h4>
<p>Continuing with the concept of KRK being used for a restaurant, a new employee would sign up for an account, and, after management verification, be allowed to log in. <i>Right now, for the live site, there is no user verification so that people may try out the system, but restricting access to only ‘verified’ employees is a simple matter to enable.</i></p>
<p>The user can then immediately access the Time Management System, which is a single click to clock in or clock out. There is a manual time edit in case the user forgot to clock in or out as well. The user has access to a profile which allows them to upload an image for their avatar, change their biography, and see all their posts, replies, and time clock punches.</p>
<p>Users can see anyone’s profile. Admins can edit anyone’s profile as well (say a user changed their username to something bad, or their avatar was not appropriate).</p>
<h4>Posting</h4>
<p>On the BBS main page is the post timeline. Employees and Supervisors only see posts from others in their own department, while Management will see all posts. Supervisors can ‘sticky’ posts for their department, which locks them to the top of the timeline and changes the formatting slightly to indicate that they are a sticky post. Storewide posts can only be added by Management and are also stuck to the top of the timeline with a slightly different format.</p>
<p>The concept of departments can be forgone as well, allowing everyone to see everyone’s posts. The system is flexible in how to handle this.</p>
<p>When making a post, the post is immediately added to the timeline. There is also an auto refresh system to update the timeline every now and then to make sure new posts from other users will be seen. <i>In the live version, this is currently disabled since, generally, there are not going to be multiple users posting at the same time, so it would be an unnecessary drain on server resources.</i></p>
<p>Posts can be replied to and favorited. Replies are handled on a post’s own page to avoid cluttering the main timeline with reply threads. Replies can have replies and be favorited. Like with Twitter, Users cannot edit posts, but can delete their own posts. Admins can delete any posts. Replies are destroyed when the parent is destroyed.</p>
<h4>Event Calendar</h4>
<p>The Event Calendar is the simplest part of the KRK application. Admins can create events, assign them dates that they will be active, and assign them to be either storewide or to single departments only (for instance, your kitchen crew would not care about training on a new cash register system).</p>
<p>These events show up, in chronological order, on the main BBS page. They disappear out of the calendar after they happen but remain in the database in case you want to simply change the dates and run them again.</p>
<h2>Under The Hood</h2>
<p>KRK is developed in Python and runs the Django backend framework. The current demo site uses Django 3.2. The front end now uses MDBootstrap 5 and regular Bootstrap 5 for styling, components, and so forth. There is not a lot of JavaScript in the app, given it’s rather simple and can mostly be handled with plain old HTML and CSS. The main BBS page uses jQuery and AJAX to process refreshing the post timeline without needing to reload the whole page.</p>
<p>I am hosting the live site on a DigitalOcean droplet. The database is a PostgreSQL database instance also hosted by DO. All static files and media are served off my DO Spaces CDN (if you inspect the page or use View Source – don’t worry, I won’t turn you over to the governor of Missouri – you will see that material comes from https://cdn.douglasavenue.com).</p>
<h2>The Future</h2>
<p>I have just gone through and redid the UI for the site, upgrading from Bootstrap 4 to the MDB5/Bootstrap 5 layout. I’ve also improved the responsiveness of the site to make it mobile-friendly.</p>
<p>I also wish to separate the front and backend at some point, relying on React for the front and Django Rest Framework on the back. This is a long-term goal. I have already done some work on that. You can feel free to look at what has been done with both the <a href="https://github.com/ewink1977/KRK-Backend" target="_blank">backend</a> and <a href="https://github.com/ewink1977/KRK-Frontend" target="_blank">frontend</a> repos.</p>
<p>In the short(ish) term, I plan on adding the following features:</p>
<ul>
  <li>Administration Dashboard. Right now, the only way to edit users is to use the Django Admin panel. This is bad as it allows too much access to the system. This will include the ability to activate and deactivate users.</li>
  <li>Friends List. I would like users to be able to add friends and see if their friends are online.</li>
  <li>Private Messaging. Users should be able to send private messages to their friends. A work-based social media app would be cool, right? You could talk to your work friends without having to friend them on Facebook, or whatever the kids these days are using.</li>
  <li>Better Time Management. I want the time management system to be able to add up hours for a week and be a system that could reasonably be used for payroll.</li>
  <li>Event RSVP. I want users to be able to indicate that they are attending an event, and those users to be shown on the event page.</li>
  <li>Better Timeline Mechanics. I would prefer that the timeline always be updated when a new post is added to the database so the client wouldn’t have to hammer the server every X seconds.</li>
</ul>
<h2>Questions/Concerns?</h2>
<p>Please email me at erin@douglasavenue.com</p>
<hr>
<p>Thanks for checking this out!</p>

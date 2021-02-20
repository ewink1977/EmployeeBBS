<h1>Employee BBS & Time Management System</h1>
    <p>ewink's Coding Dojo SOLO graduation project!</p>
        <h2> It's CRUNCH time!</h2>
            <img src="https://www.douglasavenue.com/img/mikucomputer.jpg" alt="Miku at a computer.">
            <p> I feel like this is going to be me in a few days, except I won't have anywhere near as much hair, won't be anywhere close to being as adorable as Miku is, 
                and will be a real human male, rather than a fictional girl. So, I guess that's won't be me?</p>
            <p>UPDATE: Yeah, it is me, without the kawaii...</p>
            <p>Anyway, welcome to the GitRepo for my solo graduation project.</p>
            <p>The web application is at version 1.0 right now.</p>
        <h2>Concept</h2>
            <p>When complete, this project will act as a mini-intranet Twitter style message board for a business' employees. Basically, a digital breakroom corkboard.</p>
            <p>Managers at both the department and top tier levels will be able to sticky messages and add events to the system to ensure all users see things that will be 
                affecting them and their departments.</p>
            <p>To increase the systems usefulness, there will also be a time management system built into the BBS, allowing employees to clock in and out and track their hours.</p>
                <h3>Terminology</h3>
                    <p>For the purpose of this README, there are three classes of users. <b>Superuser</b> which could be considered top-tier level management 
                        (e.g. a store's general manager). <b>Managers</b> which would run departments (e.g. a restaurant's head chef, or a shift supervisor). <b>Employees</b>, 
                        which should be considered base-level hourly staff with little or no supervisory role. <i>Admins</i>, for the purpose of this explanation, are both Superusers and 
                        Managers. <i>Users</i> are all users of the system, regardless of admin level.</p>
        <h2>Functions</h2>
            <p>There are three primary functions of the BBS:</p>
            <ul>
                <li><a href="#Dynamic">Dynamic Posting & User Profiles</a></li>
                <li><a href="#Event">Event Promotion</a></li>
                <li><a href="#TMS">Time Management System</a></li>
            </ul>
            <h3 id="Dynamic">Dynamic Posting</h3>
                <p>The purpose of the posting function on the system is to mirror a system similar to Twitter. Simple messages posted to a group.</p>
                <p>The current version (1.0) allows site management to set 'departments'. Employee level staff will only see messages from their own department on their timeline,
                    with a couple of exceptions.</p>
                <img src="http://douglasavenue.com/ebbsdoc/postclasses.jpg" alt="Posts Example" class="rounded float-left">
                <p><strong>Sticky posts</strong>, that are set by <em>admins</em>, are always at the top of the list and are not included in the pagination. They are
                    identified as sticky posts by both the <span class="text-danger">red</span> border around the post, and the red bullhorn icon in the bottom right hand corner.</p>
                <p><strong>Storewide posts</strong>, also set by <em>admins</em>, have less priority than sticky posts, and as such fall below them in the post list, but still maintain
                    priority over normal posts, so they are also not included in pagination. They have a <span class="text-warning">yellow</span> border and a yellow bullhorn icon.</p>
                <p>The difference between STICKY posts and STOREWIDE posts are that STICKY posts can be and should only be restricted to a single department. Making a storewide post
                    sticky will result in the post being double-displayed. This is something that can be possibly changed in a future version.</p>
                <p>Below the priority posts, <em>Employee</em> level posts will be displayed. These posts are paginated to make the page from being too long. In v1.0, the list will
                    update every 10 seconds.</p>
                <hr class="mx-5 border border-secondary">
                <img src="http://douglasavenue.com/ebbsdoc/postmessage.jpg" alt="How To Post" class="rounded float-left">
                <p>Posting to the main timeline happens from the main BBS page. Adding a post will refresh the post list. An <em>employee</em> level user has no control over the
                    post priority or what department the post is sent to (it will always default to the employee's department and level one (normal) post priority.</p>
                <img src="http://douglasavenue.com/ebbsdoc/postdistribution.jpg" alt="Post Distribution" class="rounded float-right">
                <p><em>Manager</em> level employees can set what department they broadcast their message to. It's important to remember that only users in the department you set
                    will be able to see a department restricted post. Only <em>manager</em> level staff have the ability to view all department posts.</p>
                <p>As well as department, managers can set whether or not the post will be stickied. Again, stickied posts should NOT be set as storwide, since those posts are
                    sticky by default. A future version of the app should have the ability to set expiration dates on the sticky/storewide posts to ensure there isn't clutter and
                    admins aren't forced to manually prune posts.</p>
                <img src="http://douglasavenue.com/ebbsdoc/postreplies.jpg" alt="Post Replies" class="rounded mx-auto d-block">
                <p>Replying to posts is as easy as clicking on the <span class="text-success">green</span> reply icon! Doing so will take the user to the post's display page, which will
                    only show the post selected and that post's replies. You can also access this page by clicking on the post date hyperlink.</p>
                <p>On the post page there is another <code>textarea</code> input box that will accept a reply to the origional message. Replies <strong>will not</strong> display
                    in the BBS main page. The number of replies are displayed, so it's a simple task to go to the post page to see the replies. </p>
                <p>Replies cannot be posted to a different department than the parent post. Replies cannot be set to sticky.</p>
                <p>Replies each have their own post page and can accept likes and replies as well. Both posts and replies can be deleted from their page. Editing posts is NOT allowed.
                    This may be changed in a future update.</p>
                    <h4>User Profiles</h4>
                    <a href="http://douglasavenue.com/ebbsdoc/updateprofile.jpg" target="_blank">
                        <img src="http://douglasavenue.com/ebbsdoc/updateprofile.jpg" alt="Update Profile" class="rounded float-left img-thumbnail" style="width: 250;"></a>
                        <p>Users are provided a profile that will allow them to upload a custom picture and set a biography. There are no programming rules to either of these fields, so they
                            would have to be set by management policy.</p>
                        <p>In v1.0, all images are resized during upload to 500px wide or 500px high, maintaining the aspect ratio. It is encouraged to use a square image so the
                            reshaping of the post avatars will still look good. </p>
                        <a href="http://douglasavenue.com/ebbsdoc/profileupdated.jpg" target="_blank">
                            <img src="http://douglasavenue.com/ebbsdoc/profileupdated.jpg" alt="Updated Profile" class="rounded float-right img-thumbnail" style="width: 250;"></a>
                        <p>After upload, images are changed postwide, so all images of the user will reflect the uploaded image.</p>
                        <p>For the demo site, images are stored off site in an Amazon S3 bucket. Old images are not deleted when no longer used, so eventually a function will need
                            to be added to handle that. A default image is provided for users that have not uploaded their own image.</p>
            <h3 id="Event">Event Promotion</h3>
                <img src="http://douglasavenue.com/ebbsdoc/eventsummary.jpg" alt="Event Summary" class="rounded float-left">
                <p>Included in the BBS Home page is an event summary box. This will display events that have been setup to be relevant for the user.</p>
                <p>Like posts, events can be set to be restricted to departments (for instance, if there is a training class for a new grill, the front of the house staff wouldn't
                    care about that or need to know). There are also storewide events which are displayed for all.</p>
                <p>The summary is not paginated, but it is reduced to only display the next 5 relevant events.</p>
                <img src="http://douglasavenue.com/ebbsdoc/eventfull.jpg" alt="Full Event Display" class="rounded mx-auto d-block">
                <p>The user has two options. They can click a link to view all the relevant posts (if there are more events than 5, otherwise the list display will be the same as
                    the BBSHome list), or they can click on the post its self and view the event details. </p>
                <p>Management level users have the ability to CREATE NEW, EDIT EVENT, or DELETE EVENT. </p>
                <p>Old events (events where the END DATE has passed) remain in the database but are no longer displayed.</p>
            <h3 id="TMS">Time Management System</h3>

<!-- <h1>Employee BBS & Time Management System</h1>
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
<p>Thanks for checking this out!</p> -->

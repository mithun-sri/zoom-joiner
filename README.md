# Zoom Joiner

<h3>Installation guide</h3>

```console
pip install -i https://test.pypi.org/simple/ zoom-joiner-mithun-sri
```

<h3>How to operate</h3>
<blockquote><b>Important</b>: It is easy to make mistakes inputting data, so if you have made a mistake inputting details, do not close the program, delete it or screw around. Refer to the <b>I made a blithering mistake</b> section at the bottom of the page.</blockquote>

Upon installing the package, there are a couple of things to do.

After installing using pip, input the following commands to first setup individual lesson details before initialising your weekly timetable.

<h4>Initialise the lesson details</h4>
Run this command first following installation to setup details regarding all your lessons.

```console
zoom-joiner --initialise lessons
```
<h4>Initialise the timetable</h4>
Run this command after initialising the lesson details as mentioned above. 

```console
zoom-joiner --initialise timetable
```
<h4>Editing a lesson</h4>

```console
zoom-joiner --edit lesson
```
<h4>Editing the timetable</h4>

```console
zoom-joiner --edit timetable
```
<h4>Deleting a lesson</h4>
<p>This command deletes the details of the lesson you select, as well as all its corresponding events in the timetable. This means the program will no longer launch lessons for this specific lesson, but will continue to do so for the other lessons.</p>

```console
zoom-joiner --del lesson
```
<h4>Deleting your timetable and all lessons</h4>
<p>This command deletes all your lessons and their corresponding details in the timetable. You can still initialise the timetable and lesson details again from scratch. <b>This doesn't uninstall the program</b></p>

```console
zoom-joiner --clear
```

You will be asked to input the number of different lessons you have. This <b>does not</b> mean enter the total number of lessons, but rather the number of unique lessons you have, each with their own unique zoom link.

For example,

```console
Enter the number of different lessons you have: 5
```

This program is only effective when the zoom links to the meeting are <b>static</b>, i.e. you use the same link to join every meeting of this respect lesson. If a particular lesson has a dynamic link, input d. It is advisable to have a seperate text document open at the same time containing a list of all your zoom links.

After declaring the number of different lessons you have, input a memorable name for the lesson (keep it as short as possible as you will have to input this again several times). After declaring the class name, enter the static zoom link for this lesson.

```console
Enter a memorable name for the lesson: AP Bio
Enter your zoom link for this lesson: https://us02web.zoom.us/j/linktomeeting
```

Repeat this process for all of your unique lessons.

<h4>Setting up daily timetable</h4>
Keep your daily timetable at hand with you. After setting up all your lesson details, you will be greeted with the following dialogue. Enter the total number of lessons you have for this particular day.

```console
Enter the number of lessons you have today: 6
```

Keep in mind, the following stage is very important and it is easy to make mistakes. The program will be looping through the number of lessons you have for today and so you <b>must</b> enter lessons in chronological order. 

```console
Enter the corresponding memorable name for this lesson: AP Bio
```

List the memorable name of the lesson as you had entered previously.  

You wil be asked to input the time this lesson takes place. <b>Use this format: HHMM</b> where hours and minutes are in 24H. Do not enter a colon or try formatting it in any other way.

```console
Enter the time the lesson begins (e.g. 0800, 1055, 1300): 1430
```

This will be a long and gruelling process but you have to list out individual details for each of your lessons for the week. Fortunately, this will be the last shed of effort you will have to apply, after which everything will be automatic. 

<h4>Using the program</h4>
The program is set to run on boot-up or at 12am everyday - whichever of the two comes first. If the program identifies that there are no meetings set for that particular day, it self-terminates and repeats this check the following day. If the program identifies that there is a meeting coming up, it will sleep in the background and run at the time when the meeting starts and joins at the prescribed time. If there are multiple meetings a day, the program runs on standby until all meetings have joined, at which point it self-terminates.

<h3>Versions</h3>
<h4>Version 1.0</h4>

- Allows users to set up their meetings and timetables
- Joins meetings at the prescribed time

The purpose of v1.0 was to test to the feasibility of the program and to identify any major setbacks which could affect the functionality of the program. Although the program worked as intended, there are still a number of issues that need to be resolved. The upcoming versions of this program hope to achieve some of the following, 
- Ability to edit meeting details such as a change in time and/or link
- Ability to delete meetings that are no longer necessary
- Improve validations and introduce redos to minimise errors in inputting details
- A set of command tools in the CLI which would allow users to opt out of particular meetings, and add stand-off meetings that are non-recurring

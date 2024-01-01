const schedule = require('node-schedule');

// custom time to run just after one minute
const newTime = new Date();
newTime.setMinutes(newTime.getMinutes() + 1);
newTime.setSeconds(0);

let job;

// scheduleJob - cron String, callback
job = schedule.scheduleJob('0 42 10 * * *', function() {
  console.log('Running Task using cron string at 10:42:00');
});

// scheduleJob - date, callback
job = schedule.scheduleJob(new Date(newTime), function() {
  console.log('Running Task using cron string at ' +newTime);
});


//------------ scheduling using recurrence rule --------------- 
// Define a recurrence rule
const rule = new schedule.RecurrenceRule();
rule.dayOfWeek = [0, new schedule.Range(4, 6)];
rule.hour = 12;
rule.minute = 30;

// Schedule the job to run on the defined schedule
job = schedule.scheduleJob(rule, function() {
  console.log('The job is running using custom rule');
});

// Cancel the job after 5 second
setTimeout(function() {
  job.cancel();
  console.log('Task canceled');
},5000);

// resheculing job
schedule.rescheduleJob(job, new Date(Date.now() + 30000));
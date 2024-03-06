import { createQueue, Job } from 'kue';

const BLACKLISTED_NUMBERS = ['4153518780', '4153518781'];
const taskQueue = createQueue();

const sendNotification = (phoneNumber, message, job, callback) => {
  let totalCount = 2;
  let remainingCount = 2;

  let sendTimer = setInterval(() => {
    if (totalCount - remainingCount <= totalCount / 2) {
      job.progress(totalCount - remainingCount, totalCount);
    }

    if (BLACKLISTED_NUMBERS.includes(phoneNumber)) {
      callback(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(sendTimer);
      return;
    }

    if (totalCount === remainingCount) {
      console.log(
        `Sending notification to ${phoneNumber},`,
        `with message: ${message}`,
      );
    }

    --remainingCount || callback();
    remainingCount || clearInterval(sendTimer);
  }, 1000);
};

taskQueue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
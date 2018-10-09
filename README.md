[![praxtrain.com](https://image.ibb.co/eBt9EK/praxlogo.png "praxtrain.com")](http://praxtrain.com "praxtrain.com")

###About

PraxTrain is a devotional guide for people wanting to study and learn from the Bible on a daily basis, developed for Antioch New England. Content is managed by the director of Antioch Discipleship School. Users are able to subscribe to daily emails with the day&apos;s &quot;Praxis&quot;, which may include Bible reading, memorization, contemplation, reflection, intercessory prayer and faith activation. 


###Details

PraxTrain is hosted on AWS Elastic Beanstalk with the Flask backend and SQlite3 database for subscribers. Emails are scheduled on the same server on a threaded process, scheduled for 8pm EST. Email server is hosted on [Zoho](http://zoho.com "Zoho") and sent over a TLS port. Email HTML is generated using [mj-ml](https://mjml.io/). 

###Future Features
- [x] Google Sheets API connection for content generation
- [x] jQuery for responsive elements
- [x] Email sending task scheduled and generated
- [ ] HTTPS connection
- [ ] User interaction including progress tracking and group forums
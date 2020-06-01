# OPvCon_registrator
A script for parsing a dump of info from Mailchimp into workshop schedules for the [OpenPlanetary Virtual Conference (OPvCon, June 22-24, 2020)](https://www.openplanetary.org/vcon).

A lot of the mess is around figuring out which workshop to put people in when they signed up for two or more that overlap at the same time. It also prints out form text for each registrant to make them easy to email, and also produces summaries of attendees for each workshop to give to each host. (I sorted the .CSV by registration time in LibreOffice first so that earlier registrants get priority.)

This whole thing is unlikely to be useful to anyone else. But I spent several hours on it, and it definitely won't be useful to anybody else if I don't put it into public. It might be a good example of why you should scriptify things, even if messily. I thought about doing this by hand, but this approach ended up being faster and allowed me to iterate on ideas about how to resolve schedule conflicts.

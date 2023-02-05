## rateMyLinkedIn

About: This project is the start of a tool that will rate a LinkedIn user's profile by utlizing openai's gpt-3 engine: text-davinci-003, along with prompt engineering for users to get vital feedback on their profile.

Why: Linkedin is the number one tool for finding and getting hired for jobs. Every hiring manager or recruiter has a linkedIn, and they will be checking out profiles for potential talent. So essentially it is the first representation of oneself that a recruiter or a potential hiring manager will see. If LinkedIn is used right, the amount of interviews, or the number of opportunities can increase. With the help of rateMyLinkedIn (this project) users can receive feedback on certain parts of their profile and be able to optimize it.

To Implement: 
-Build a nice ui/frontend for users to interact with 
-More Prompt Engineering
-More data to work with, so far this script looks at just the summary of a profile.

Api's Used:
[query LinkedIn data (not official doc)](https://linkedin-api.readthedocs.io/en/latest/api.html)
[click for original github for the linkedin api](https://github.com/tomquirk/linkedin-api)
[openai api doc](https://platform.openai.com/docs/api-reference?lang=python)
[openai github](https://github.com/openai/openai-python)

## Example of a prompt: 
A good linkedin profile summary includes a greeting, one's professional interest or current focus, one's personal interests (optional), and one's contact information. 
A good example of this is: 
(greeting) Thanks for taking the time to get to know me through my Linkedin profile. I appreciate you stopping by!
(professional interest or current focus) Professionally, I am passionate about creating and delivering meaningful learning experiences that help sales professionals use LinkedIn Sales Navigator to target, understand, and engage their prospects and customers.
(personal interests (optional)) Personally, I'm a high energy person with a passion for building relationships through genuine interests in others. I am a proud father to a daughter and son, who keep my wife and I busy, while bringing us entertainment and joy. I enjoy spending time outdoors (golfing, running), weightlifting, NFL football (Go Birdz!), and listening to great music.
(contact information) Feel free to send me a personalized connection request or contact me directly at ...email.com if you wish to discuss mutual areas of interest or to learn more.
Rate the following prompt on a scale of 1 to 5, where 1 represents unsatisfactory and 5 is exemplary from the above analysis and include an analysis of what the prompt should include and why: 

I'm a second-year attending Temple University majoring in Computer Science.

Output from gpt-3:
2: This prompt is missing essential information to be considered a good LinkedIn profile summary. It is missing a greeting, a professional interest or current focus, personal interests (optional), and contact information. A good summary should include details that make the reader want to learn more about the individual, such as their professional accomplishments, relevant experience, and current goals. This is important for creating an engaging profile that will help the individual stand out from the competition.

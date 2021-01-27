# WasteMaster-CruzHacks

75% of ALL trash is recyclable, yet we only recycle 30% of it due to inconvenience and a lack of knowledge in recycling. WasteMaster is a ML appl. which helps classify trash and correctly recycle it.

Inspiration: My mom was throwing away the trash, and I noted that so many recyclable waste was merely thrown in the trash. We conducted research on how much recyclable trash is being thrown away and realized a common reason why people don't recycle is due to inconvenience of classifying the trash. We aim to reduce the amount of misclassified trash that is being thrown out, an hopefully reduce waste and emissions through such an application.

What it does: WasteMaster helps classify the trash into its appropriate categories: Misc. Trash, Recycling, Composting. This can allow the user to simply throw the trash into its appropriate bin without having to consider regulations and rules on which items can be recycled.

How We built it : WasteMaster was built using the Trashnet dataset from Stanford and Google AutoML. We hypertuned the model to maximize the precision and recall to both around 92% and with an overall accuracy of 97%. After building the model, we connected it to a web application with a front end and backend which communicated with the AutoML API.

Challenges We ran into : We had trouble deploying the app on Google Cloud, so we had to demo it on local host. There were numerous problems with installation requirements, flask version etc. which didn't allow us to upload and publish it on Google Cloud. However we believe that our video shows a great demo of how it would classify trash, had it been deployed for public access.

Accomplishments that We're proud of : We are very proud of our perseverance in curating, cleaning and labelling the dataset. We've developed a greater understanding of how ML works and the parameters which can be tuned. We also developed skills in full stack development when we built the web application.

What I learned : I learned how to make a backend using Flask, use AutoML and front end development using HTML, CSS and Bootstrap. We also learned the importance of communication especially during a virtual Hackathon. In fact, we made an effort to stay on our zoom call for the last 48 hours of the hackathon, to simulate the real feeling of the hackathon and also strengthen our communication and team morale.

What's next for WasteMaster : We would love to deploy it on Google Cloud and have an option to view nearby recycling centers for those without recycling bins in their homes. This would allow even more people to recycle and help save the one and only earth that we dearly love.


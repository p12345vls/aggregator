# aggregator
An aggregator is a program that systematically compiles a specific type of information from multiple online sources.The aggregator will take a filename and a topic as command line arguments.  The file will contain a possibly very long list of online sources (urls).  The topic will be a string such as flu, football, etc...Our aggregator will open and read the urls contained in the file, and it will report back on the subset of urls that contain a reference to the specified topic.  The program will put the output in a text file.  That output will contain both the urls and the text containing the reference. The output file will be created in the working directory.  Its name will consist of the topic followed by summary.txt.  So when the topic is flu, the output filename will be flusummary.txt, when the topic is football, the output filename will be footballsummary.txt.
<img width="1071" alt="screen shot 2017-09-30 at 4 06 50 pm" src="https://user-images.githubusercontent.com/32381448/31050248-e5dc203a-a5f9-11e7-817c-1e8cc10bcc77.png">
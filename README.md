# crewai-Playground

This will be my playground for all things to do with crewai.

## Tuesday, November 19, 2024

 1) mamba create -n crewai python=3.11
 2) conda activate crewai
 3) mamba install conda-forge::jupyterlab
 4) mamba install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
 5) pip install crewai  ... version 0.80.0 ... this installed a ton of stuff!! 
 6) pip install 'crewai[tools]' ... version 0.14.0

We are going to step through the Matthew Berman video [Step-by-Step Langtrace + CrewAI Tutorial - Production Agent Stack](https://www.youtube.com/watch?v=dh9zv8EUwBA) as a start to this project.

 Now we will generate a use crewai to create a demo app ... and just to be safe, I am going to run this command from the repository folder.

 7) crewai create crew demo-app

 This asks me to select a provider (I selected ollama), and then a model (I selected ollama/llama3.1). This generates the 'demo_app' sub folder.

 Next, we go into that 'demo_app' folder, and then run the command ....
 
 8) cd demo_app
 9) crewai install 

 This again loads a ton of stuff, and once it has finished, you then run ...

 10) crewai run

 Hmm ok something is not working, so how do we get this working with ollama??

 OK Nice! I got the crew working with Ollama running locally! I am guessing getting it to work against KAUWITB should be as easy as setting the ip ...

 ## Wednesday, November 20, 2024

 So I am attempting to run the demo_app against LMStudio locally, and it runs without errors, even though I do not have LMStudio running! OK! It is still using the OpenAI API for this! Wow! ... good to know!

 OK That's interesting! CrewAI will spin up the ollama model if it is not already running! And the model value set in crew.py DOES drive which model gets loaded, NOT what is set in .env ...

 OK. Gonna start using LangTrace. Created a new account using my google account.

 11) pip install langtrace-python-sdk

 OK. So I've messed something up here. The crewai code that generated the demo-app wrote into a python virtual environment, so I don't need to be using mamba or conda for this stuff. I am gonna torch everything (except this repostory) and start over.

 Whelp, turns out there was no need for this! [Default CrewAI virtual environment - Conflict with Conda](https://community.crewai.com/t/default-crewai-virtual-environment-conflict-with-conda/1116) The LangTrace stuff is now working! Great!

 ## Friday, November 22, 2024

 Gonna give [FireCrawl Scrape Website](https://docs.crewai.com/tools/firecrawlscrapewebsitetool) a go ... 

 12) pip install firecrawl-py 'crewai[tools]' # this installed firecrawl-py-1.5.0

 ## Saturday, November 23, 2024

 Hmm thinking of exploring Scrapy to .... scrape a website. But isn't this repo about CrewAI??

 13) mamba install conda-forge::scrapy # this installed scrapy-2.12.0

 ## Tuesday, December 31, 2024

 Getting back to this ... how do I spin stuff up?? 

  1) run 'crewai run' from the root folder? Nope! 
  2) mamba activate crewai, and then run 'crewai run' from the root folder? Nope! Gonna look at the video ... 
  3) move into the 'demo_app' folder, and then run 'crewai run' ... Yup! That now works! And it is running locally using ollama.

  Right! So how do I switch over to LMStudio?? ... Wait ... where can I see the LangTrace stuff?? Right ... langtrace.ai ... sign in with your github account ...

  OK! So how can I use LMStudio?? Hmm for now, I am gonna stear clear of that question, just because it is working locally with ollama and I can see all the trace information with langtrace.









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

  Hmm gonna install the latest version of CrewAI ... currently in the crewai conda environment, we are at crewai 0.80.0, and crewai-tools 0.14.0

  14) pip install crewai --upgrade

  And now we are at crewai 0.86.0 and crewai-tools 0.17.0 

  Nice. Running 'crewai run' from within the demo_app folder still runs without errors. And just to see how the demo_app may differ, I am going to run ...

  crewai create crew demo_app_2 ... selecting 'ollama' as the provider, and 'ollama/mixtral' as the model.

  I also ran 'ollama run mixtral'.

  ## Wednesday, January 1, 2025

  Right. I tried to use the langtrace stuff in demo_app_2 but it was not finding the package, so the solution was once again to implement the solution found [here](https://community.crewai.com/t/default-crewai-virtual-environment-conflict-with-conda/1116)

I ran 'ollama run mixtral:8x22b' on KAUWITB ... I should be able to acces this via Ollama by just changing the ip in demo_app_2/.env, right?? Hmm, apparently it does not! Surprising!

Sigh ... that model was too big for KAUWITB ... so I killed it. Gonna pull down 'ollama run mixtral' and try that.

Gonna give [Langfuse](https://langfuse.com/) a go today ... by [running Langfuse locally](https://langfuse.com/self-hosting/local). I really want to be able to run everything locally.

Yup! That spins up effortlessly! And looks real nice. Gonna Remove langtrace stuff from demo_app_2 and get it to use langfuse.

Wow really!?? There does not appear to be any CrewAI integration with Lanfuse! WTF!!? I see Langfuse has integrations with Langchain, Langserve, Haystack, LLamaindex and a bunch of other way more obscure packages, but NOTHING for CrewAI!

Looks like I need to install langfuse to the project ...

15) pip install  langfuse

Sigh. I cannot get langfuse stuff to work within demo_app_2, so I am just going to continue using langtrace just becase it is already working. 

Yeah so every time I re-run the app, the 'report.md' file gets regenerated with different content. Is this ONLY using parametric knowledge, or is search being used? Wow, is all of this every 'black boxy' for me! Like WTF is going on? How is stuff being called? I am guessing looking at the langtrace stuff could provide insight into this. My first impression of all of this is that CrewAI is NOT using search, meaning it is not using any search tool to find relevant docs on the internet.

Hmm the latest CrewAI is no longer using poerty for dependency management, but now uses [UV](https://docs.astral.sh/uv/). 

"🚀 A single tool to replace pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, and more."

Hmm so it looks like UV is way faster than pip, poetry or virtualenv ... yeah, gonna actually create something newer for all of this CrewAI stuff ... but keep the code in this repo. I also think this may make stuff easier to replicate between the kitchen computer and KAUWITB. I also think it can replace conda/mamba.

OK. Opened up a new terminal window, then ran the following commands :

 1) mamba deactivate                                 # deactivates any mamba silliness that may get in the way.
 2) curl -LsSf https://astral.sh/uv/install.sh | sh  # installs uv
 3) uv                                               # validates that uv has been installed.
 4) pip install 'crewai[tools]'                      # installs crewai and crewai[tools]
 5) pip freeze | grep crewai                         # checks the installed versions.

    rob@rob-MS-7C91:~$ pip freeze | grep crewai
    crewai==0.86.0
    crewai-tools==0.17.0 

Now make sure the current terminal window is in the root folder of the 'CrewAI-Playground' repository, and then run ...

 6) crewai create crew latest-ai-development

 This will first ask 'Select a provider to set up:'

    Select a provider to set up:
    1. openai
    2. anthropic
    3. gemini
    4. groq
    5. ollama
    6. watson
    7. bedrock
    8. azure
    9. cerebras
    10. other
    q. Quit

I picked 1, for openai, because I want to see what it generates.

Then it asked:

  Select a model to use for Openai:
  1. gpt-4
  2. gpt-4o
  3. gpt-4o-mini
  4. o1-mini
  5. o1-preview
  q. Quit

I selected 3, gpt-40-mini.

Then it asked:

Enter your OPENAI API key (press Enter to skip): 

I pressed Enter to skip this step.

 7) cd latest-ai-development
 8) crewai install                      # this installs a ton of stuff REALLY FAST! WOW IS UV FAST!
 9) crewai run                          # this runs the crew and generates the report.md file.

This will be the first call I have made to OpenAI this year! Wow! The total cost for that run was less than a penny!

## Thursday, January 2, 2025

Gonna rerun latest_ai_development using GPT-4 to see the results. Wow! Gpt-4 cost $0.12 ! ... sure it is still cheap, but it is way more expensive than gpt-40-mini

OK. So I tried to run latest-ai-development using langtrace but it can't find the module. Do I use UV to import langtrace?

Disable the langtrace stuff, then change .env to use local ollama with mixtral works fine. So how do I get it to work nicely with langtrace? OK! Right! The solution was to modify the .venv/pyvenv.cfg file to include-system-site-packages = true from false.

BTW using ollama/mixtral locally puts a huge load on all 16 cores of the cpu as well as taking up about 5.5gb of vram. Nice to see ollama offloads stuff to the cpu when there is not enough gpu vram!

Why does changing the .env file from ...

    MODEL=ollama/mixtral
    API_BASE=http://localhost:11434

... to ... 

    MODEL=ollama/mixtral
    API_BASE=http://192.168.2.16:11434

... NOT result in using Ollama on KAUWITB?? This SILL uses the local machine! I don't get it!? .. 

So re-running 'crewai run' again and again ... shows you will never get the same resulting 'report.md' and that the results differ vastly from one run to the next. The question I have is are the results from parametric knowledge or from search? Hmm well looking at the [Serper Dashboard](https://serper.dev/dashboard) reveals I have not made any calls yet to this service ... so it must be parametric knowledge!

Hmm I am going to try a different model to see how the results differ. Can I just pick any model available from Ollama?? Gonna download and try [dolphin-mixtral](https://ollama.com/library/dolphin-mixtral)

Just out of curiosity, when I spin up a new crewai and select the Ollama provider, I get the following Ollama models:

    Select a model to use for Ollama:
    1. ollama/llama3.1
    2. ollama/mixtral
    q. Quit

Yup! ollama/dolphin-mixtral works just fine!

Hmm so how easy is it to swtich from, say openai or ollama, to, say, groq?

crewai create crew groq ... 

        Select a model to use for Groq:
        1. groq/llama-3.1-8b-instant
        2. groq/llama-3.1-70b-versatile
        3. groq/llama-3.1-405b-reasoning
        4. groq/gemma2-9b-it
        5. groq/gemma-7b-it
        q. Quit

When I select groq, I get the above models as options. Hmm I selected 3, and then it asked for my Groq key ... I provided this. Wow ... looking at the generated code, I can see that key has been written into the .env file. That is way to insecure for my liking! But let's give it go, shall we ...?

I terminalled into the new groq folder, and then ran 'crewai install' ... this installs a ton of dependencies using UV for dependency management. Now will tweak the .venv/pyvenv.cfg file to 'include-system-site-packages = true' and then run 'crewai run' to see if it runs. Hmm Nope! Looking at the console log, I can see that the model 'groq/llama-3.1-405b-reasoning' has been 'decommissioned and is no longer supported'. Looking at [groq supported models](https://console.groq.com/docs/models) I will tweak the .env file to change 'MODEL=groq/llama-3.1-405b-reasoning' to 'MODEL=groq/llama3-70b-8192' and then run 'crewai run' again ... Nice! That ran, and damn, is it ever fast! Now gonna bake in langtrace and run it again. Yup! The groq project now works with langtrace and uses groq! Nice! 

So before I commit this new groq code, I am gonna kill that working key from the .env file. Wait! I don't need to do this, because that file is ignored by git by default! Nice! 

OK Nice! I cloned this repo to KAUWITB, set stuff up and was able to 'crewai run' the groq project!

Gonna crewai run latest_ai_development on KAUWITB using ollama/mixtral ... Yeah, so each crewai folder has its own .venv folder that gets generated when you run 'crewai install' ... the contents of this folder are NOT saved into github, cuz it would be just too damn big. So on every workstation where you clone this repo, you will have to manually create the .env file for the environment variables, and run 'crewai install' to load the project dependencies, and then tweak the .venv/pyvenv.cfg file to 'include-system-site-packages = true'

Hmm so the latest_ai_development crewai ollama mixtral project DOES run on KAUWITB ... all 8 cpu cores are heavily utilized and gpu vram usage is 22578mib. And it took a looong time to run! ... guessing over 5 minutes!










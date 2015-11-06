FROM python:3-onbuild

# Run the python script
CMD [ "python", "./twitchcounts.py" ]

#### README
#### Summary
This is a sample command line application for concurrently crawling web links in Internet folder.
##### Assumptions
1. The application will be run on Python 2.7
2. The format of all .json files are consistent and the "Internet" is made of those files in Internet folder.
3. Run time is not a big issue. And so performance optimization was a not primary consideration.

#### Reasons for any significant design choices you made
1. For the purpose of keeping the code concise for this project, I implemented a boss-worker concurrency model where each worker gets a file path and former the same job.

# class4-homeworks
# Continouse Integration (CI)

CI is the proccess of automating the build and testing of code every time (several times per day) a team member commits changes to version control. CI significantly helps to share your 
code and unit tests by 
merging your changes into a shared version control repository after very small task completion.
Without that, intergrating code that is written by developers creats many merge confilicts, hard to fixbugs and it takes a lot of time.

The benefits:

- Fast feedback loop
- Increase transparency and visibility
- Detect and fix issues early  

How it works:

CI keeps the master branch clean. Teams can leverage modern version control systems such as Git to create short-lived feature branches to isolate their work. A developer submits a 
“pull request” when the feature is complete and, on approval of the pull request, the changes get merged into the master branch. Then the developer can delete the previous feature 
branch. Development teams repeat the process for additional work. The team can establish branch policies to ensure the master branch meets desired quality criteria.
 
My preference tool:

After doing a research, I found many tools that we can use as a CI with GitHub. I prefer JenKins as a developer becuse:
- It's free.
- It offers flexibility to implement any customer use case.
- It has a great documentation.
- Easily configurable.
- And Docker in conjunction with Jenkins is having a profound effect on development teams.Together Docker, Jenkins and its integrated ecosystem provide the coordinating software 
  infrastructure for agile development (resource for this point https://apiumhub.com/tech-blog-barcelona/advantages-of-jenkins/).

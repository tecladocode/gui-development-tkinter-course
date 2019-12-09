# Building for multiple platforms

As we've mentioned before, to build an executable for a platform, PyInstaller must be ran on that platform.

No way around it, so you must get access to a target platform Operating System to build.

You could do this using a Continuous Integration solution like AppVeyor or CircleCI. In them, you can specify the Operating System that will run your code. Do note that you may have to pay for some of this functionality.

Although we won't cover how, the general process goes as follows:

- Create your AppVeyor or CircleCI account;
- Link your GitHub repository with it so it knows when there are code changes;
- Configure your AppVeyor or CircleCI project so that it uses your target operating system;
- Configure your AppVeyor or CircleCI project so that it runs PyInstaller;
- Make the resultant `dist` folder available somewhere for download by your users (an option is Amazon's S3).
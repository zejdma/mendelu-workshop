# Repository for Mendel University workshop files

This repository contains files and instructions for students to run a few
examples with OpenShift and Quay demonstrating some of the DevOps principles -
automation and self-healing/no support architectures

There are total of 3 examples to do.

## Contents

* Dockerfile - instructions for Docker/Podman to build a container image from
               this repository
* openshift-template.yaml - Template to deploy this application in OpenShift
* cgi-bin/form.py - gets `value` GET parameter and stores it in
       `/dev/shm/countdown`
* backend.py - periodically looks for `/dev/shm/countdown` and generates
       `/dev/shm/output` based on this file
* cgi-bin/display.py - shows current content of `/dev/shm/output`

Files above have number of ugly bugs. Most of them are intentional :-)

## Preparation

You will not need everything initially but this is a list of dependencies for
going through these examples:

* Have OpenShift Clients (oc) binary. Can be downloaded from [release page](https://github.com/openshift/origin/releases/tag/v3.11.0)
* Get [Github.com](https://github.com) account
* Get [OpenShift.io](https://openshift.io) account
* Get [Quay.io](https://quay.io) account

## Running the code on your own VM

Beware - the code can trigger out of memory situations.

* Running server part: `python3 -m http.server --cgi 9000`
* Running backend: `python3 backend.py`
* Client: browser/curl

You can clean up after testing by removing following files:

* `/dev/shm/countdown`
* `/dev/shm/output`

## Part 1 - Automatic builds

This example should show you how you can have automatically built production
code on every commit in your repository without manual intervention. This saves
time and prevents manual errors.

### Steps for Part 1

* Fork this repository into your own space on Github
* Create new repository on Quay (plus sign at top-right)
  * Pick a name (mendelu-workshop?)
  * Make sure to make repository "Public"
  * Use "Link to a GitHub Repository Push"
  * Pick your fork of this repository
  * Pick "Trigger for all branches and tags"
  * Select Dockerfile path (`/Dockerfile`)
  * Select Context (`/`)
* Test the setup by pushing a new change to your fork

Bonus: Use `podman run -it <url> /bin/bash` to verify

## Part 2 - Deploy working application

This part will show you that deploying a fresh application can be quick and
consistent. Once deployed in OpenShift the example application is more resilient
to bugs.

### Steps for Part 2

* Go to [openshift.io](https://openshift.io/) and sign up.
  * Note - the process will ask for your phone number to prevent duplicate
    sign-ups
* Create a new "Space" from your code on Github
* After creation go to "Analyze" tab
* At the bottom part of the page "Pipelines" should have build. Go to "Build #1"
* At the top right - click your name and "Copy login command"
* Run this command in your VM
  * This will require that you set up "oc" as described above
* Run `oc process -f openshift-template.yaml | oc apply -f -`

After a while if you go to "Overview" back in your browser, you should get a URL
to your container application. You can play with `cgi-bin/form.py/?value=<XX>`
and `cgi-bin/display.py` URLs.

Bonus: Fix the bug that was shown during introduction/demo

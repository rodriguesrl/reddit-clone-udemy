=============================
Reddit Clone Improvement
=============================

.. image:: https://img.shields.io/pypi/l/django-fine-uploader.svg

After finishing the Reddit Clone challenge i noticed that upvoting or downvoting from the user page would redirect to the home page and i made a quick fix for that, checking where the vote came from and redirecting to the correct page. I would like to share the project to help anyone with the same problem,feel free to use this repository as you want :D

Quick Fix
----------

The fix is basically sending "home" or "userpage" along with the forms of voting and then checking inside the views.py, really simple and fast, so let's go to the step-by-step:

- Inside your ``home.html`` add another hidden input to both Upvote and Downvote forms:

.. code-block:: html

    <input type="hidden" name="from" value="home">

- Inside your ``userposts.html`` (i called mine byuser.html) add another hidden input to both Upvote and Downvote forms:

.. code-block:: html

    <input type="hidden" name="from" value="user">

- Inside your Posts app ``views.py``, change the Upvote and Downvote functions to check the input we just added:

.. code-block:: python

    if request.POST['from'] == 'home':
      return redirect('home')
    else:
      #Remember to change the page names to yours :D
      return redirect('posts:byuser', userid=post.author.id)
      
- Thats it! Go ahead and give it a try :D

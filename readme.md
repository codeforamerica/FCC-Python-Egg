FCC Python Egg
=======
A Python wrapper for the FCC Reboot APIs.

Does your project or organization use this gem?
------------------------------------------
Add it to the [apps](https://github.com/codeforamerica/FCC-Python-Egg/wiki) wiki!

Installation
------------
    $ [sudo] python setup.py install

Usage Examples
--------------
    import broadband_api

    # Create an object to interface with the Broadband API
	bb = BroadbandApi()

    # Get the data!
    print bb.get_data(latitude=37, longitude=-122) # (Should be San Francisco)

    # Most of the rest is done the same way...

    # Make a License View API object
    lv = LicenseViewAPI()

    # Use it!
    lv.get_licenses(searchValue = "Verizon Wireless")


FCC API Docs
------------
1. [Broadband Speed Test](http://www.fcc.gov/developer/consumer-broadband-test-api)
2. [License View](http://www.fcc.gov/developer/license-view-api)
3. [Census Block](http://www.fcc.gov/developer/census-block-conversions-api)
4. [FCC Registration Number Conversions](http://www.fcc.gov/developer/frn-conversions-api)

    
Contributing
------------
In the spirit of [free software](http://www.fsf.org/licensing/essays/free-sw.html), **everyone** is encouraged to help improve this project.

Here are some ways *you* can contribute:

* by using alpha, beta, and prerelease versions
* by reporting bugs
* by suggesting new features
* by writing or editing documentation
* by writing specifications
* by writing code (**no patch is too small**: fix typos, add comments, clean up inconsistent whitespace)
* by refactoring code
* by resolving [issues](http://github.com/cfalabs/fcc_reboot/issues)
* there won't be any issues, but we are obligated to say that anyway
* by reviewing patches

Submitting an Issue
-------------------
We use the [GitHub issue tracker](http://github.com/cfalabs/fcc_reboot/issues) to track bugs and
features. Before submitting a bug report or feature request, check to make sure it hasn't already
been submitted. You can indicate support for an existing issuse by voting it up. When submitting a
bug report, please include a [Gist](http://gist.github.com/) that includes a stack trace and any
details that may be necessary to reproduce the bug, including your gem version, Ruby version, and
operating system. Ideally, a bug report should include a pull request with failing specs.

Submitting a Pull Request
-------------------------
1. Fork the project.
2. Create a topic branch.
3. Implement your feature or bug fix.
4. Add documentation for your feature or bug fix.
5. Run <tt>bundle exec rake doc:yard</tt>. If your changes are not 100% documented, go back to step 4.
6. Add specs for your feature or bug fix.
7. Run <tt>bundle exec rake spec</tt>. If your changes are not 100% covered, go back to step 6.
8. Commit and push your changes.
9. Submit a pull request. Please do not include changes to the gemspec, version, or history file. (If you want to create your own version for some reason, please do so in a separate commit.)

Copyright
---------
Copyright (c) 2010 Code for America Laboratories
See [LICENSE](https://github.com/cfalabs/fcc_reboot/blob/master/LICENSE.mkd) for details.
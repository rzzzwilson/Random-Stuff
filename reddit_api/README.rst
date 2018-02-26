Some simple code investigating using the Reddit API.

Some beginning, non-PRAW, code here:

http://www.pythonforbeginners.com/python-on-the-web/how-to-use-reddit-api-in-python/

Format of JSON return for username/comments::

    {'data': {'after': 't1_duu8dne',
              'before': None,
              'children': [<comment>, <comment>],
              'dist': 2,
              'modhash': '',
              'whitelist_status': None},
     'kind': 'Listing'}

Where a <comment> has the form::

    {'data': {'approved_at_utc': None,
              'approved_by': None,
              'archived': False,
              'author': 'rzzzwilson',
              'author_flair_css_class': None,
              'author_flair_text': None,
              'banned_at_utc': None,
              'banned_by': None,
              'body': 'Good.  Now you have to fix that '
                      'negative sum.  Hint: look at how you '
                      'calculated the sum of the positive '
                      'numbers.',
              'body_html': '&lt;div '
                           'class="md"&gt;&lt;p&gt;Good.  '
                           'Now you have to fix that '
                           'negative sum.  Hint: look at '
                           'how you calculated the sum of '
                           'the positive '
                           'numbers.&lt;/p&gt;\n'
                           '&lt;/div&gt;',
              'can_gild': True,
              'can_mod_post': False,
              'collapsed': False,
              'collapsed_reason': None,
              'controversiality': 0,
              'created': 1519653698.0,
              'created_utc': 1519624898.0,
              'distinguished': None,
              'downs': 0,
              'edited': False,
              'gilded': 0,
              'id': 'duu9g3a',
              'is_submitter': False,
              'likes': None,
              'link_author': 'jamescain27',
              'link_id': 't3_80a7iq',
              'link_permalink': 'https://www.reddit.com/r/learnpython/comments/80a7iq/stuck_trying_to_solve_this/',
              'link_title': 'Stuck trying to solve this',
              'link_url': 'https://www.reddit.com/r/learnpython/comments/80a7iq/stuck_trying_to_solve_this/',
              'mod_note': None,
              'mod_reason_by': None,
              'mod_reason_title': None,
              'mod_reports': [],
              'name': 't1_duu9g3a',
              'num_comments': 7,
              'num_reports': None,
              'over_18': False,
              'parent_id': 't1_duu8rpy',
              'permalink': '/r/learnpython/comments/80a7iq/stuck_trying_to_solve_this/duu9g3a/',
              'quarantine': False,
              'removal_reason': None,
              'replies': '',
              'report_reasons': None,
              'saved': False,
              'score': 1,
              'score_hidden': False,
              'stickied': False,
              'subreddit': 'learnpython',
              'subreddit_id': 't5_2r8ot',
              'subreddit_name_prefixed': 'r/learnpython',
              'subreddit_type': 'public',
              'ups': 1,
              'user_reports': []},
     'kind': 't1'},
    {'data': {'approved_at_utc': None,
              'approved_by': None,
              'archived': False,
              'author': 'rzzzwilson',
              'author_flair_css_class': None,
              'author_flair_text': None,
              'banned_at_utc': None,
              'banned_by': None,
              'body': 'When I run the code I posted, I '
                      'get:\n'
                      '\n'
                      '    $ python3 test.py \n'
                      '    Please enter number 1: 1\n'
                      '    Please enter number 2: 2\n'
                      '    Please enter number 3: 3\n'
                      '    Please enter number 4: 4\n'
                      '    sumAll = 10.0\n'
                      '    sumPos = 10.0\n'
                      '    sumNeg = 0\n'
                      '\n'
                      'so make sure that what you are '
                      'running is what you posted.  It '
                      '*should* be, but I get a different '
                      'result.\n'
                      '\n'
                      'Guessing as to what the problem is: '
                      'note that the result you print, 4, '
                      'is the last number you entered.  Are '
                      "you sure that your code doesn't have "
                      'these last lines:\n'
                      '\n'
                      '    print("sumAll =", value)\n'
                      '    print("sumPos =", value)\n'
                      '\n'
                      'or the line that sums the numbers '
                      "isn't:\n"
                      '\n'
                      '    sumAll = value   # note: missing '
                      "'+'\n"
                      '\n'
                      'PS:\n'
                      'The suggestion from '
                      '/u/ViridianHominid is a good one - '
                      'put print statements in your code to '
                      'help debug a problem.  In this case, '
                      '`sumAll` is wrong, so put these '
                      'lines around where you update '
                      '`sumAll` to see if the updating is '
                      'correct:\n'
                      '\n'
                      "    print('before: sumAll=%f, "
                      "value=%f' % (sumAll, value))\n"
                      '    sumAll += value # add every '
                      'value to sumAll\n'
                      "    print('after: sumAll=%f' % "
                      'sumAll)',
              'body_html': '&lt;div '
                           'class="md"&gt;&lt;p&gt;When I '
                           'run the code I posted, I '
                           'get:&lt;/p&gt;\n'
                           '\n'
                           '&lt;pre&gt;&lt;code&gt;$ '
                           'python3 test.py \n'
                           'Please enter number 1: 1\n'
                           'Please enter number 2: 2\n'
                           'Please enter number 3: 3\n'
                           'Please enter number 4: 4\n'
                           'sumAll = 10.0\n'
                           'sumPos = 10.0\n'
                           'sumNeg = 0\n'
                           '&lt;/code&gt;&lt;/pre&gt;\n'
                           '\n'
                           '&lt;p&gt;so make sure that what '
                           'you are running is what you '
                           'posted.  It '
                           '&lt;em&gt;should&lt;/em&gt; be, '
                           'but I get a different '
                           'result.&lt;/p&gt;\n'
                           '\n'
                           '&lt;p&gt;Guessing as to what '
                           'the problem is: note that the '
                           'result you print, 4, is the '
                           'last number you entered.  Are '
                           'you sure that your code '
                           'doesn&amp;#39;t have these last '
                           'lines:&lt;/p&gt;\n'
                           '\n'
                           '&lt;pre&gt;&lt;code&gt;print(&amp;quot;sumAll '
                           '=&amp;quot;, value)\n'
                           'print(&amp;quot;sumPos '
                           '=&amp;quot;, value)\n'
                           '&lt;/code&gt;&lt;/pre&gt;\n'
                           '\n'
                           '&lt;p&gt;or the line that sums '
                           'the numbers '
                           'isn&amp;#39;t:&lt;/p&gt;\n'
                           '\n'
                           '&lt;pre&gt;&lt;code&gt;sumAll = '
                           'value   # note: missing '
                           '&amp;#39;+&amp;#39;\n'
                           '&lt;/code&gt;&lt;/pre&gt;\n'
                           '\n'
                           '&lt;p&gt;PS:\n'
                           'The suggestion from &lt;a '
                           'href="/u/ViridianHominid"&gt;/u/ViridianHominid&lt;/a&gt; '
                           'is a good one - put print '
                           'statements in your code to help '
                           'debug a problem.  In this case, '
                           '&lt;code&gt;sumAll&lt;/code&gt; '
                           'is wrong, so put these lines '
                           'around where you update '
                           '&lt;code&gt;sumAll&lt;/code&gt; '
                           'to see if the updating is '
                           'correct:&lt;/p&gt;\n'
                           '\n'
                           '&lt;pre&gt;&lt;code&gt;print(&amp;#39;before: '
                           'sumAll=%f, value=%f&amp;#39; % '
                           '(sumAll, value))\n'
                           'sumAll += value # add every '
                           'value to sumAll\n'
                           'print(&amp;#39;after: '
                           'sumAll=%f&amp;#39; % sumAll)\n'
                           '&lt;/code&gt;&lt;/pre&gt;\n'
                           '&lt;/div&gt;',
              'can_gild': True,
              'can_mod_post': False,
              'collapsed': False,
              'collapsed_reason': None,
              'controversiality': 0,
              'created': 1519652002.0,
              'created_utc': 1519623202.0,
              'distinguished': None,
              'downs': 0,
              'edited': 1519623591.0,
              'gilded': 0,
              'id': 'duu8dne',
              'is_submitter': False,
              'likes': None,
              'link_author': 'jamescain27',
              'link_id': 't3_80a7iq',
              'link_permalink': 'https://www.reddit.com/r/learnpython/comments/80a7iq/stuck_trying_to_solve_this/',
              'link_title': 'Stuck trying to solve this',
              'link_url': 'https://www.reddit.com/r/learnpython/comments/80a7iq/stuck_trying_to_solve_this/',
              'mod_note': None,
              'mod_reason_by': None,
              'mod_reason_title': None,
              'mod_reports': [],
              'name': 't1_duu8dne',
              'num_comments': 7,
              'num_reports': None,
              'over_18': False,
              'parent_id': 't1_duu7t08',
              'permalink': '/r/learnpython/comments/80a7iq/stuck_trying_to_solve_this/duu8dne/',
              'quarantine': False,
              'removal_reason': None,
              'replies': '',
              'report_reasons': None,
              'saved': False,
              'score': 2,
              'score_hidden': False,
              'stickied': False,
              'subreddit': 'learnpython',
              'subreddit_id': 't5_2r8ot',
              'subreddit_name_prefixed': 'r/learnpython',
              'subreddit_type': 'public',
              'ups': 2,
              'user_reports': []},
     'kind': 't1'}],

# Simple JOSE JWE example

Install python jwcrypto
```
% pip install jwcrypto
```

Run from cli
```
% python ./jws-in-jwe.py
JWS: {"header":{"alg":"HS256"},"payload":"eyJkb2IiOiIyOC8wOS8xOTkwIiwiZW1haWwiOiJ6dWxmaWthckBva2Fkb2MuY29tIiwiZXhwaXJlZCI6IjIwMjQtMDMtMTFUMTM6NDA6MTErMDM6MDAiLCJmZ19wYXltZW50IjoxLCJnZW5kZXIiOiJNYWxlIiwiaSBkZW50aXR5X2lkIjoiNzg0MTk5MDEyNDM1NzYxIiwiaWRlbnRpdHlfdHlwZV9pZCI6MSwibGF0aXR1ZGUiOjI1LjI5MTIyODM2OTQ4MTcwNCwibG9uZ2l0dWRlIjo1NS4zODQwMTUyOTE5MjkyNDUsIm1lbWJlcklEYXBwb2ludG1lbnQiOjEzMjIsIm1lbWJlcklEc2VuZGVyIjoxMzIyLCJtb2JpbGVudW1iZXIiOiI5NzE0NDg0NzQ2NDYiLCJuYW1lIjoiVGV1a3UgWnVsZmlrYXIgQW1pbiIsIm5ldHdvcmtJRCI6MTE5fQ","signature":"p6uOSM6CB10Yx6u50hKno5LkD0y4nEb1xmmRyqDUy9g"}

JWE: eyJhbGciOiJkaXIiLCJjdHkiOiJKV1QiLCJlbmMiOiJBMTI4R0NNIiwiemlwIjoiREVGIn0..9wuYHZs-fDJSgn5C.3NyBkJvr4__W4DE69KeU82_yrsEleaWS7DnSulC3HnECLbXvdzDSvqg-JsSXG4Fwv4OUswbwmIPj6gEezlS3JD8VvHbUYJLxo2zDI_RFYkjA8n9xMW1QnupfD2YsYcjtvXrT9VGcNDza5DojUL-waBHb6R_grZtWaP-QMGSwJen28xFj5tupk--FAavAxv2ZQ9e1-UMyDXT58WWHNBc4hbjC8dS2BbEOKu5ha0fbm3ZYo6cTHvK4kZKTbXUby7BUCyufCNaUA9IwgZhtlHlTsXfWxuDGZZYrmRSEz0B_3M49c9UFILRCQoqDOYNcFomKa0l5V9git4GiSC6b5YEnpgY7d-IcUfMjtY5twZUZAT9FxTYGoq3aqTPSFhqOsZeUlI0sDi1_UQovwEb6vGpy8RGVZ_8RPDMO0A8dCCN4MD22hiHZbEtcT7h838s-lnq5WR-WLAZeckmtFuYcTWkPjFPMVI0ix4E6mlyJjSPeA8F0MWFpiYTJ4x9UVHbqAmqQjwjp2sL5a0rWS1nQqgan5gDjk4HGY-x4HUIHYFyIXG3Y8nwG42O8eWF45cS8b1cFgoQThco.d47a1yGUNIuZmy0w-XUQbA
```

source:

- https://github.com/latchset/jwcrypto
- https://jwcrypto.readthedocs.io/en/latest/ß
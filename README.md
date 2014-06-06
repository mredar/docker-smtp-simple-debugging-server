docker-smtp-simple-debugging-server
===================================

Docker for python stdlib smtpd.DebuggingServer (https://docs.python.org/2/library/smtpd.html).
Outputs email to stdout and then discards message.  Great for development.

docker run -d -p 25:25 <image_name or id>
docker logs <containter> to see email messages.

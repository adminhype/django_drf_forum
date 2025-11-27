from rest_framework.throttling import UserRateThrottle


class QuestionThrottle(UserRateThrottle):
    scope = 'question'

    # def allow_request(self, request, view):
    #     request_method = 'question-' + request.method.lower()

    #     if request.method == 'GET':
    #         return True

    #     if request_method in self.THROTTLE_RATES:
    #         self.scope = request_method
    #         self.rate = self.get_rate()
    #         self.num_requests, self.duration = self.parse_rate(self.rate)
    #     return super().allow_request(request, view)


class QuestionGetThrottele(UserRateThrottle):
    scope = 'question-get'


class QuestionPostThrottle(UserRateThrottle):
    scope = 'question-post'

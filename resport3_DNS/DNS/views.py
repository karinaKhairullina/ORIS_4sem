import dns.resolver
from django.http import JsonResponse

def lookup(request, domain):
    try:
        ip = [str(ip) for ip in dns.resolver.resolve(domain, 'A')]
        return JsonResponse({'ip': ip})
    except Exception as e:
        return JsonResponse({'error': str(e)})

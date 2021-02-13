<!-- Row 1 - Demo description -->
{{ description }}

<!-- Row 2 - Shields to display demo information -->
<span style="display:block;text-align:center">
  <a href="{{ costLink }}">
    <img src="https://img.shields.io/badge/Cost-${{ cost }}/month-{% if cost < 101 %}success{% elif cost < 1000 %}orange{% else %}critical{% endif %}" />
  </a>
  <img src="https://img.shields.io/badge/Time-{{ time }} minutes-{% if time < 10 %}success{% elif time < 30 %}orange{% else %}critical{% endif %}" />
</span>

<!-- Row 3 - Deploy to Azure button -->
<span style="display:block;text-align:center">
  <a href="https://portal.azure.com/#create/Microsoft.Template/uri/{{ armLink | urlencode | replace("/", "%2F") }}" target="_blank">
    <img src="https://aka.ms/deploytoazurebutton"/>
  </a>
</span>

<!-- Row 4 - Links to Azure documentation, GitHub, and Share -->
<span style="display:block;text-align:center">
  <a href="{{ documentationLink }}">
    <img width="25px" src="http://www.pngpix.com/wp-content/uploads/2016/07/PNGPIX-COM-Microsoft-Logo-Icon-PNG-Transparent.png">
  </a>
  <a href="{{ githubLink }}">
    <img width="25px" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png">
  </a>
  <a target="_self" href="">
    <img height="25px" src="https://opsgility.com/Images/azure-icons/azure-logo.png">
  </a>
  <a target="_self" href="">
    <img height="25px" src="https://static.djangoproject.com/img/logos/django-logo-negative.png">
  </a>
  <a href="mailto:robertlacher@microsoft.com?subject={{ mailToSubject}}&body={{ mailToBody | urlencode | replace ("/", "%2F") }}">
    <img src="https://img.shields.io/badge/Share-informational?logo=mail.ru" height="25px"/>
  </a>
</span>
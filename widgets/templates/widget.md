<!-- Row 1 - Links to Azure documentation, GitHub, and Share -->
<span style="display:block;text-align:center">
  <a href="{{ documentationLink }}">
    <img width="25px" src="https://github.com/ralacher/azure-dashboards/blob/main/widgets/images/microsoft.png?raw=true">
  </a>
  <a href="{{ githubLink }}">
    <img width="25px" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png">
  </a>
  <a href="mailto:?subject={{ title }}-{{ subtitle }}&body=Links%20from%20our%20discussion%20today.%0A%0ADocumentation%0A{{ documentationLink | urlencode | replace ("/", "%2F") }}%0A%0AGitHub%20Code%0A{{ githubLink | urlencode | replace ("/", "%2F") }}%0A%0ACost%20Estimate%0A{{ costLink | urlencode | replace ("/", "%2F") }}">
    <img src="https://freepngimg.com/thumb/logo/64838-icons-symbol-envelope-computer-mail-logo-email.png" height="25px"/>
  </a>
  <a href="https://portal.azure.com/#create/Microsoft.Template/uri/{{ armLink | urlencode | replace("/", "%2F") }}" target="_blank">
    <img height="25px" src="https://aka.ms/deploytoazurebutton"/>
  </a>
</span>
<!-- Row 2 - Shields to display demo information -->
<span style="display:block;text-align:center">
  <a href="{{ costLink }}">
    <img src="https://img.shields.io/badge/Cost-${{ cost }}/month-{% if cost < 101 %}success{% elif cost < 1000 %}orange{% else %}critical{% endif %}" />
  </a>
  <img src="https://img.shields.io/badge/Time-{{ time }} minutes-{% if time < 10 %}success{% elif time < 30 %}orange{% else %}critical{% endif %}" />
</span>

<!-- Row 3 - Demo description -->
{{ description }}

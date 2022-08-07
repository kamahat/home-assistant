# Home-Assistant-Swiming-Pool-Manager-HASPo


[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

This not yet custom component for Home Assistant can be used to automatically control a pool pump driven by temperature, recovre data from pH and ORP prob to drive acid or chloric pump. Get swiming pool energy consumption, manager water level

This developpement follows
 0 - logic issue from Abacus: https://github.com/scadinot/pool.
 
 1 - 1st version done by @exxamalte](https://github.com/exxamalte/home-assistant-customisations/tree/master/pool-pump).
 
 2 - reworking of ha-pool_pump from [@oncleben31] (https://github.com/oncleben31/ha-pool_pump)
 
 3 - new version done by [@remycrochon] using python (doc un FR : https://domo.rem81.com/tag/piscine/ ) (https://github.com/remycrochon/home-assistant/blob/master/packages/ph.yaml)
 
 4 - reworking of version from [@remycrochon]
 
## Minimum requirements

* A Home Assistant runing installation : every thing can be simulated
* have the HA addon : Appdaemon (https://github.com/hassio-addons/addon-appdaemon)
* have the Telegram plugin for alerts
* A switch supported in Home Assistant that can turn on/off power to your pool pump.

## Features

* Can control any switch that drive the pool pump .
    * Summer mode 
		* with 2 ways of control 
			* based on temperature divide by 2 
			* or Abacus 
		* Splits the target duration into two equal runs with a break in between and print it in HA
		* add a time filtration coef beteween 60 and 140%
		* end filtration at 23:59:59
    * Force On: Turn switch on.
    * Force Off: Turn switch off.
	* Winter mode

* Optional: Support for a water level sensor 
* Optional: pH sensor witch optionaly can active a pump 
* Optional: ORP sensor witch optionaly can activate a chloric pump
* Optional: active a switch which drive the swiming pool cover
* Optional: mesure energy consumption

## Caveats

* Does not currently consider solar electricity production.
* lot of thing written in french, need internationalisation

## Installation

### HACS installation

Not yet

### Manual installation

1) If not done install appdaemon : https://appdaemon.readthedocs.io/en/latest/INSTALL.html

2) configuration.yaml
you need to ahve these lines in /config/configuration.yaml
```yaml
packages: !include_dir_named integration
automation manual: !include_dir_merge_list automations/
automation ui: !include automations.yaml
```
config yaml files are in /config/integration
automation manual files are in /config/integreation/automations


3) clone the directory

4) go to appdaemon/apps/filtration_piscine.yaml and set your
- swiming pool temp sensor : "sensor.temp_piscine"
- pump switch "switch.ppe_filtration"

## Front-end

It use Dwains dashboard v3
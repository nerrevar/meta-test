<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style lang="sass">
*
  margin: 0
  padding: 0

#app
  width: 100%
  min-height: 100vh

  display: flex
  flex: 1 1 auto
  flex-flow: column nowrap
  align-items: center

.wrapper
  display: flex
  flex: 0 0 auto
  flex-flow: column nowrap

  padding: 1.5rem

.main-title
  display: flex
  flex: 1 0 auto
  flex-flow: column nowrap
  align-items: center

  padding: 0.5rem

.button-block
  display: flex
  flex: 0 0 auto
  flex-flow: row nowrap
  justify-content: space-between

.button
  display: flex
  flex: 0 0 auto
  flex-flow: column nowrap
  align-items: center

  padding: 0.5rem

  color: grey
  text-decoration: none
  background-color: lightgreen

  box-shadow: 3px 3px 5px lightgrey

  &:disabled
    color: grey
    background: lightgrey
</style>

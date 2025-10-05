(function () {
  const root = document.getElementById('toast-root');
  const template = document.getElementById('toast-template');
  if (!root || !template) return;

  function pickIcon(type) {
    if (type === 'success') return '✅';
    if (type === 'error') return '⛔';
    if (type === 'warning') return '⚠️';
    if (type === 'info') return 'ℹ️';
    return '🔔';
  }

  function setTypeStyles(el, type) {
    el.classList.remove('bg-white', 'border-gray-200', 'text-gray-800');
    el.classList.remove('bg-green-50', 'border-green-400', 'text-green-800');
    el.classList.remove('bg-red-50', 'border-red-400', 'text-red-800');
    el.classList.remove('bg-yellow-50', 'border-yellow-400', 'text-yellow-800');
    if (type === 'success') el.classList.add('bg-green-50', 'border-green-400', 'text-green-800');
    else if (type === 'error') el.classList.add('bg-red-50', 'border-red-400', 'text-red-800');
    else if (type === 'warning') el.classList.add('bg-yellow-50', 'border-yellow-400', 'text-yellow-800');
    else el.classList.add('bg-white', 'border-gray-200', 'text-gray-800');
  }

  window.showToast = function (title, message, type = 'info', duration = 4000) {
    const node = template.content.firstElementChild.cloneNode(true);
    node.querySelector('[data-title]').textContent = title || '';
    node.querySelector('[data-message]').textContent = message || '';
    node.querySelector('[data-icon]').textContent = pickIcon(type);
    setTypeStyles(node, type);

    const closeBtn = node.querySelector('[data-close]');
    const remove = () => {
      node.classList.add('opacity-0', 'translate-y-3');
      node.classList.remove('opacity-100', 'translate-y-0');
      setTimeout(() => node.remove(), 180);
    };
    closeBtn.addEventListener('click', remove);

    root.appendChild(node);
    requestAnimationFrame(() => {
      node.classList.add('opacity-100', 'translate-y-0');
      node.classList.remove('opacity-0', 'translate-y-3');
    });

    if (duration > 0) setTimeout(remove, duration);
  };
})();

function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    
    if (!toastComponent) return;

    // Remove all type classes first
    toastComponent.classList.remove(
        'bg-red-50', 'border-red-500', 'text-red-600',
        'bg-green-50', 'border-green-500', 'text-green-600',
        'bg-white', 'border-gray-300', 'text-gray-800'
    );

    // Set type styles and icon
    if (type === 'success') {
        toastComponent.classList.add('bg-green-50', 'border-green-500', 'text-green-600');
        toastComponent.style.border = '1px solid #22c55e';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-red-50', 'border-red-500', 'text-red-600');
        toastComponent.style.border = '1px solid #ef4444';
    } else {
        toastComponent.classList.add('bg-white', 'border-gray-300', 'text-gray-800');
        toastComponent.style.border = '1px solid #d1d5db';
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}